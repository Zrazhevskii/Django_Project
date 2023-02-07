from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters, DateTimeFromToRangeFilter, DateFromToRangeFilter, CharFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    creator = CharFilter(field_name='creator', lookup_expr='exact')
    status = CharFilter(field_name='status')
    updated_at = filters.DateFromToRangeFilter()

    # created_at = filters.DateFromToRangeFilter()
    # creator = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ('creator', 'status', 'created_at', 'updated_at')
