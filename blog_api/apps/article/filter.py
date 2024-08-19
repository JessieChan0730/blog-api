from django_filters import rest_framework as filters

from .models import Article


class CategoryFilter(filters.FilterSet):
    category = filters.NumberFilter(method='filter_by_category_id')

    def filter_by_category_id(self, queryset, name, value):
        if value:
            return queryset.filter(category_id=value)
        return queryset

    class Meta:
        model = Article
        fields = ["category"]
