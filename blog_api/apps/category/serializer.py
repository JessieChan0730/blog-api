from rest_framework import serializers

from category.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=10, read_only=True,required=False)
