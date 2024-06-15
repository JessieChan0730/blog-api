from rest_framework import serializers

from tag.models import Tag


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=10, read_only=True,required=False)
