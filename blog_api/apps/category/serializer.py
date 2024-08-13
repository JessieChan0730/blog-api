from django.conf import settings
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10, required=True)
    display = serializers.BooleanField()

    def create(self, validated_data):
        name = validated_data.get("name")
        display = validated_data.get("display")
        category = Category.objects.create(name=name, display=display)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.display = validated_data.get("display", instance.display)
        instance.save()
        return instance

    def validate_display(self, value):
        if value:
            # 主页展示不能超过4个
            setting_len = settings.BLOG_SETTINGS.get("HOME_DISPLAY", 4)
            if len(Category.objects.filter(display=1)) >= setting_len:
                raise serializers.ValidationError(f"主页展示不能大于{setting_len}个")
        return value


class DeleteMultiple(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField(), required=True, allow_empty=False, min_length=1)
