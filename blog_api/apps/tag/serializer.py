from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, required=True)
    color = serializers.CharField(max_length=8, required=False, default='#409EFF')

    def create(self, validated_data):
        name = validated_data.get("name")
        color = validated_data.get("color")
        tag = Tag.objects.create(name=name, color=color)
        return tag

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.color = validated_data.get("color", instance.color)
        instance.save()
        return instance

