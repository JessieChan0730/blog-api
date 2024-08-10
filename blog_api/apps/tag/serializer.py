from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, required=True)

    def create(self, validated_data):
        name = validated_data.get("name")
        tag = Tag.objects.create(name=name)
        return tag

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class DeleteMultiple(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField(), required=True, allow_empty=False, min_length=1)
