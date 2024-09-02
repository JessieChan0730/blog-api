from rest_framework import serializers

from .models import BlogSettings


class MetaSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=25, required=False)
    cover = serializers.ImageField(required=False, label="图片", use_url=True, error_messages={
        'invalid': '图片参数错误'
    })

    def create(self, validated_data):
        title = validated_data.get("title", None)
        cover = validated_data.get("cover", None)
        meta = BlogSettings.objects.first()
        # 不存在就创建
        if meta is None:
            meta = BlogSettings(title=title, cover=cover)
            meta.save()
            return meta
        if title:
            meta.title = title
        if cover:
            meta.cover = cover
        meta.save()
        return meta


class PutSettingSerializer(serializers.ListSerializer):
    id = serializers.IntegerField(label="配置ID")
    value = serializers.IntegerField(label="配置值")

    def update(self, instance_queryset, validated_data_list):
        pass



