from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    # creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        status_count = Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN').count()
        query = self.context["request"]
        if status_count > 10 and query.method == 'POST' and data['status'] == 'OPEN':
            raise ValidationError('Превышен лимит объявлений со статусом "OPEN"')
        elif status_count > 10 and (query.method == 'PATCH' or query.method == 'PUT') and data['status'] == 'OPEN':
            raise ValidationError('Превышен лимит объявлений со статусом "OPEN"')
        return data
