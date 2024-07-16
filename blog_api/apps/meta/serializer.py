from rest_framework import serializers

from .models import BlogMeta


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'cover']
        model = BlogMeta
