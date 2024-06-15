from django.contrib.auth.models import User
from rest_framework import serializers
from article.models import Article
from category.serializer import CategorySerializer
from tag.serializer import TagSerializer
from user.serializer import UserSerializer

from category.models import Category

from tag.models import Tag


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=40, required=True, label='标题')
    content = serializers.CharField(allow_blank=False, allow_null=False, required=True, label='内容')
    intro = serializers.CharField(allow_blank=False, allow_null=False, required=True, label='简介')
    cover = serializers.StringRelatedField(label='封面')
    is_recommend = serializers.BooleanField(default=False, required=False, label='是否推荐')
    category_id = serializers.IntegerField(min_value=1, write_only=True)
    tags_ids = serializers.ListField(min_length=1, allow_empty=False, allow_null=False, write_only=True)

    # 以下数据不需要用户上传
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    author = UserSerializer(required=False)
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    # 验证分类是否存在
    def validate_category_id(self, value):
        if not Category.objects.filter(pk=value).exists():
            raise serializers.ValidationError("分类不存在")
        return value

    # 验证tag是否存在
    def validate_tags_ids(self, value):
        # 数据库中查询已存在的id
        existing_ids = Tag.objects.filter(pk__in=value).values_list('id', flat=True)
        # 清理出不存在的ID
        non_existing_ids = set(value) - set(existing_ids)
        if len(non_existing_ids) > 0:
            raise serializers.ValidationError(f"分类ID：{non_existing_ids}不存在")
        return value

    def create(self, validated_data):
        # 视图传递
        author = validated_data.get('author')
        category_id = validated_data.get('category_id')
        tags_ids = validated_data.get('tags_ids')

        title = validated_data.get('title')
        content = validated_data.get('content')
        intro = validated_data.get('intro')
        cover = validated_data.get('cover')
        is_recommend = validated_data.get('is_recommend')

        category = Category.objects.get(pk=category_id)
        tags = Tag.objects.filter(pk__in=tags_ids)

        article = Article.objects.create(title=title, content=content, intro=intro, cover=cover,
                                         is_recommend=is_recommend,
                                         category=category, author=author)
        for tag in tags:
            article.tags.add(tag)

        return article

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
