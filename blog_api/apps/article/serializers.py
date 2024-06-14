from rest_framework import serializers

from article.models import Article

from category.serializer import CategorySerializer

from tag.serializer import TagSerializer
from user.serializer import UserSerializer


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=40, required=True)
    content = serializers.CharField(allow_blank=False, allow_null=False, required=True)
    intro = serializers.CharField(allow_blank=False, allow_null=False, required=True)
    cover = serializers.ImageField()
    is_recommend = serializers.BooleanField(default=False, required=False)
    categories = CategorySerializer()
    tags = TagSerializer(many=True)

    author = UserSerializer()
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    def create(self, validated_data):
        return Article.objects.create(**validated_data, author=validated_data['author'])

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.intro = validated_data.get('intro', instance.intro)
        instance.cover = validated_data.get('cover', instance.cover)
        instance.is_recommend = validated_data.get('is_recommend', instance.is_recommend)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

