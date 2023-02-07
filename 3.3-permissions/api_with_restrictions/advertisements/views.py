from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import AccessPermission
from advertisements.serializers import AdvertisementSerializer


# class AdvertisementListViewSet(ModelViewSet):
#     queryset = Advertisement.objects.all()
#     serializer_class = AdvertisementSerializer
#     permission_classes = (IsAdminOrReadOnly,)
#

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    # permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        if self.action in ["create"]:
            permissions = [IsAuthenticated]
        elif self.action in ["update", "partial_update", "destroy"]:
            permissions = [AccessPermission]
        else:
            permissions = []
        return [permission() for permission in permissions]



#Users f9a97466e3cba7008cd32da01d63ee3be3b6de5e
# Admin 55dc273db6b947e36b983a3987f81333edf3a809