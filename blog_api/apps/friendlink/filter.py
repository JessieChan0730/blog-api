from django_filters import rest_framework as filters

from .models import FriendLink


class FriendLinkFilter(filters.FilterSet):
    name = filters.CharFilter(method='filter_by_name')
    status = filters.CharFilter(method='filter_by_status')

    def filter_by_name(self, queryset, name, value):
        if value:
            return queryset.filter(name__icontains=value)
        return queryset

    def filter_by_status(self, queryset, name, value):
        if value:
            return queryset.filter(status=value)
        return queryset

    class Meta:
        model = FriendLink
        fields = ["name", "status"]
