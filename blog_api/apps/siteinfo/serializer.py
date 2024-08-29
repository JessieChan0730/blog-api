from rest_framework import serializers

from .models import SiteInfo


class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteInfo
        fields = '__all__'
        read_only_fields = ('id',)
