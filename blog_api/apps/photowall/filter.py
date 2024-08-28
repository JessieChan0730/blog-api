from django_filters import rest_framework as filters

from .models import PhotoWall


class PhotoWallFilter(filters.FilterSet):
    description = filters.CharFilter(method='filter_by_description')

    def filter_by_description(self, queryset, name, value):
        if value:
            return queryset.filter(description__icontains=value)
        return queryset

    class Meta:
        model = PhotoWall
        fields = ["description"]
