from django_filters import rest_framework as filters

from .models import Category


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(method='filter_by_name')

    def filter_by_name(self, queryset, name, value):
        if value:
            return queryset.filter(name__icontains=value)
        return queryset

    class Meta:
        model = Category
        fields = ["name"]

