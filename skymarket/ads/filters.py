from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from ads.models import Ad


class AdFilter(FilterSet):
    title = CharFilter(field_name='Title', lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ['title']
