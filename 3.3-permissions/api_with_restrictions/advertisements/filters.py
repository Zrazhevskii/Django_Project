from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters, DateTimeFromToRangeFilter

from advertisements.models import Advertisement

User = get_user_model()


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter()
    creator = filters.ModelChoiceFilter(queryset=User.objects.all())

    # TODO: задайте требуемые фильтры
    # created_at_before = filters.DateFromToRangeFilter(field_name='created_at_before', lookup_expr='gte', )
    # created_at_after = filters.DateFromToRangeFilter(field_name='created_at_after', lookup_expr='lte', )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)
