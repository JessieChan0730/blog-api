import re

from category.models import Category
from category.serializer import CategorySerializer
from rest_framework import serializers
from tag.models import Tag
from tag.serializer import TagSerializer
from user.serializer import UserSerializer

from .models import Article, ImageContent, Cover


# 创建接口
class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1, read_only=True)
    title = serializers.CharField(min_length=1, max_length=40, label='标题')
    content = serializers.CharField(allow_blank=False, allow_null=False, label='内容')
    intro = serializers.CharField(allow_blank=False, allow_null=False, max_length=200, label='简介')
    cover_url = serializers.URLField(required=True, label='封面链接')
    recommend = serializers.BooleanField(default=False, required=False, label='是否推荐')
    visible = serializers.BooleanField(label='是否可见', required=False, default=True)
    category_id = serializers.IntegerField(min_value=1, write_only=True)
    tags_ids = serializers.ListField(min_length=1, allow_empty=False, allow_null=False, write_only=True)

    # 以下数据不需要用户上传
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    author = UserSerializer(read_only=True)
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
        # TODO 去除表情包
        clearn_emoji = re.compile(u'['
                                  u'\U0001F300-\U0001F5FF'  # 杂项符号和象形图  
                                  u'\U0001F600-\U0001F64F'  # 表情与情感  
                                  u'\U0001F680-\U0001F6FF'  # 运输和地图符号  
                                  u'\u2600-\u26FF'  # 杂项符号  
                                  u'\u2700-\u27BF'  # 括号、括号装饰符等  
                                  # ... 可以根据需要添加更多范围  
                                  u']+')
        content = re.sub(clearn_emoji, '', validated_data.get('content', ''))  # 正则匹配，将表情符合替换为空''
        intro = validated_data.get('intro')
        cover_url = validated_data.get('cover_url')
        visible = validated_data.get('visible')
        recommend = validated_data.get('recommend')

        category = Category.objects.get(pk=category_id)
        article = Article.objects.create(title=title, content=content, intro=intro, cover_url=cover_url,
                                         recommend=recommend,
                                         category=category, author=author, visible=visible)

        tags = Tag.objects.filter(pk__in=tags_ids)
        for tag in tags:
            article.tags.add(tag)

        return article

    def update(self, instance, validated_data):
        # 没传递则采用原来的数据
        instance.title = validated_data.get('title', instance.title)
        # TODO 去除表情包
        clearn_emoji = re.compile(u'['
                                  u'\U0001F300-\U0001F5FF'  # 杂项符号和象形图  
                                  u'\U0001F600-\U0001F64F'  # 表情与情感  
                                  u'\U0001F680-\U0001F6FF'  # 运输和地图符号  
                                  u'\u2600-\u26FF'  # 杂项符号  
                                  u'\u2700-\u27BF'  # 括号、括号装饰符等  
                                  # ... 可以根据需要添加更多范围  
                                  u']+')
        instance.content = re.sub(clearn_emoji, '', validated_data.get('content', ''))  # 正则匹配，将表情符合替换为空''
        instance.intro = validated_data.get('intro', instance.intro)
        instance.cover_url = validated_data.get('cover_url', instance.cover_url)
        instance.recommend = validated_data.get('recommend', instance.recommend)
        instance.visible = validated_data.get('visible', instance.visible)

        category_id = validated_data.get('category_id', None)
        if category_id is not None:
            instance.category = Category.objects.get(pk=category_id)

        tags_ids = validated_data.get('tags_ids', None)
        if tags_ids is not None:
            # 获取文章模型中所有的旧的ID
            model_tags_ids = instance.tags.values_list('id', flat=True)
            set_tags_ids = set(tags_ids)
            set_model_tags_ids = set(model_tags_ids)
            # 求出需要新增的ID集合
            add_ids = set_tags_ids - set_model_tags_ids
            # 求出保留的ID
            kept_ids = set_tags_ids & set_model_tags_ids
            # 求出需要更新的ID列表
            update_ids = list(add_ids | kept_ids)
            # 删除旧的依赖关系
            instance.tags.clear()
            # 设置新的依赖关系
            tags = Tag.objects.filter(id__in=update_ids)
            instance.tags.set(tags)

        instance.save()
        return instance


# 更新接口
# class ArticleUpdateSerializer(serializers.Serializer):
#     id = serializers.IntegerField(min_value=1, read_only=True)
#     title = serializers.CharField(required=False, min_length=1, max_length=40, label='标题')
#     content = serializers.CharField(required=False, allow_blank=False, allow_null=False, label='内容')
#     intro = serializers.CharField(required=False, allow_blank=False, allow_null=False, max_length=200, label='简介')
#     cover_url = serializers.URLField(required=False, label='封面链接')
#     recommend = serializers.BooleanField(default=False, required=False, label='是否推荐')
#     visible = serializers.BooleanField(label='是否可见', required=False, default=True)
#     category_id = serializers.IntegerField(required=False, min_value=1, write_only=True)
#     tags_ids = serializers.ListField(required=False, min_length=1, allow_empty=False, allow_null=False, write_only=True)
#
#     # 以下数据不需要用户上传
#     category = CategorySerializer(read_only=True)
#     tags = TagSerializer(read_only=True, many=True)
#     author = UserSerializer(read_only=True)
#     create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
#     update_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
#
#     # 验证分类是否存在
#     def validate_category_id(self, value):
#         if not Category.objects.filter(pk=value).exists():
#             raise serializers.ValidationError("分类不存在")
#         return value
#
#     # 验证tag是否存在
#     def validate_tags_ids(self, value):
#         # 数据库中查询已存在的id
#         existing_ids = Tag.objects.filter(pk__in=value).values_list('id', flat=True)
#         # 清理出不存在的ID
#         non_existing_ids = set(value) - set(existing_ids)
#         if len(non_existing_ids) > 0:
#             raise serializers.ValidationError(f"分类ID：{non_existing_ids}不存在")
#         return value
#
#     def update(self, instance, validated_data):
#         # 没传递则采用原来的数据
#         instance.title = validated_data.get('title', instance.title)
#         # TODO 去除表情包
#         instance.content = regex.sub(r'\p{Emoji}+', '-', validated_data.get('content', instance.content))
#         instance.intro = validated_data.get('intro', instance.intro)
#         instance.cover_url = validated_data.get('cover_url', instance.cover_url)
#         instance.recommend = validated_data.get('recommend', instance.recommend)
#
#         category_id = validated_data.get('category_id', None)
#         if category_id is not None:
#             instance.category = Category.objects.get(pk=category_id)
#
#         tags_ids = validated_data.get('tags_ids', None)
#         if tags_ids is not None:
#             # 获取文章模型中所有的旧的ID
#             model_tags_ids = instance.tags.values_list('id', flat=True)
#             set_tags_ids = set(tags_ids)
#             set_model_tags_ids = set(model_tags_ids)
#             # 求出需要新增的ID集合
#             add_ids = set_tags_ids - set_model_tags_ids
#             # 求出保留的ID
#             kept_ids = set_tags_ids & set_model_tags_ids
#             # 求出需要更新的ID列表
#             update_ids = list(add_ids | kept_ids)
#             # 删除旧的依赖关系
#             instance.tags.clear()
#             # 设置新的依赖关系
#             tags = Tag.objects.filter(id__in=update_ids)
#             instance.tags.set(tags)
#
#         instance.save()
#         return instance


# 文章图片上传接口
class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ['image']


# 文章封面上传接口
class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        fields = "__all__"
