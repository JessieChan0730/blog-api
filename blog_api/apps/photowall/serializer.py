from rest_framework import serializers

from .models import PhotoWall


class PhotoWallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoWall
        fields = '__all__'
        read_only_fields = ['id']
        extra_kwargs = {
            'image': {'use_url': True},
            'visible': {'default': True},
        }


class FrontPhotoWallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoWall
        fields = ['id', 'image','description']
        read_only_fields = ['id']
        extra_kwargs = {
            'image': {'use_url': True},
        }


class PhotoWallUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(max_length=255, label="图片介绍")
    visible = serializers.BooleanField(default=True, label="是否可见")

    def update(self, instance, validated_data):
        for field in self.fields:
            if field in validated_data:
                setattr(instance, field, validated_data[field])
        instance.save()
        return instance


# TODO 抽取到公共APP中
class DeleteMultiple(serializers.Serializer):
    ids = serializers.ListField(child=serializers.IntegerField(), required=True, allow_empty=False, min_length=1)
