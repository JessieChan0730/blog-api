from rest_framework import serializers

from .models import BlogMeta


class MetaSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=25, required=False)
    cover = serializers.ImageField(required=False, label="图片", use_url=True, error_messages={
        'invalid': '图片参数错误'
    })

    def create(self, validated_data):
        title = validated_data.get("title", None)
        cover = validated_data.get("cover", None)
        meta = BlogMeta.objects.first()
        # 不存在就创建
        if meta is None:
            meta = BlogMeta(title=title, cover=cover)
            meta.save()
            return meta
        if title:
            meta.title = title
        if cover:
            meta.cover = cover
        meta.save()
        return meta
