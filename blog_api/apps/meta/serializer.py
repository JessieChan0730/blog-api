from rest_framework import serializers
from .models import BlogMeta


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = BlogMeta
