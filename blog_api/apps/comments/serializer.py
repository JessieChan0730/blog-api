from django.contrib.auth.models import User
from rest_framework import serializers
from user.models import UserDetail

from blog_api.utils.email import send_email
from .filter import SensitiveFilter
from .models import Comments


# 共同字段
class BaseCommentsSerializer(serializers.ModelSerializer):
    reply_comments = serializers.SerializerMethodField()
    parent_comment_nickname = serializers.SerializerMethodField()
    article_name = serializers.SerializerMethodField()
    Filter = SensitiveFilter()

    # def __init__(self):
    #     self.Filter = SensitiveFilter()
    #     super(BaseCommentsSerializer, self).__init__()

    def get_reply_comments(self, obj):
        # 这里我们序列化 obj.replies.all()，即当前评论的所有子评论
        # 使用相同的 CommentSerializer，但设置 depth=1 来避免无限递归（尽管在这个例子中我们不会直接用到它）
        # 实际上，对于每个序列化器实例，我们不会直接传递 depth 参数，而是通过全局设置或视图中的配置来处理
        reply_serializers = FrontCommentSerializer(obj.replies.all(), many=True)
        return reply_serializers.data

    def get_parent_comment_nickname(self, obj):
        return obj.parent_comment.nickname if obj.parent_comment is not None else None

    def get_article_name(self, obj):
        return obj.article_pk.title if obj.article_pk is not None else ""


# 后端序列化器
class AdminCommentSerializer(BaseCommentsSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'article_pk', 'article_name', 'nickname', 'avatar', 'email', 'content', 'notification',
                  'parent_comment',
                  'parent_comment_nickname', 'admin_comment', 'create_time', 'reply_comments']
        # 评论深度，从参数暂定
        deep = 1
        read_only_fields = ['id', 'nickname', 'avatar', 'admin_comment', 'article_name', 'parent_comment_nickname',
                            'reply_comments',
                            'create_time']
        extra_kwargs = {
            'email': {'required': False},
        }

    def create(self, validated_data):
        # 获取当前用户详情
        user_detail = UserDetail.objects.first()
        article_pk = validated_data.get("article_pk")
        nickname = user_detail.nickname
        email = User.objects.first().email
        content = self.Filter.replaceSensitiveWord(validated_data.get("content"))
        notification = validated_data.get("notification", True)
        avatar = user_detail.avatar.url
        parent_comment = validated_data.get("parent_comment")
        comments = Comments.objects.create(article_pk=article_pk, nickname=nickname, content=content, avatar=avatar,
                                           parent_comment=parent_comment, admin_comment=True, notification=notification,
                                           email=email)
        # 发送邮件
        if comments.parent_comment is not None and comments.parent_comment.notification:
            message = f"{comments.nickname}给您回复：{comments.content}"
            send_email(title="您在JBlog的评论收到回复啦", message=message,
                       target=comments.parent_comment.email)
        return comments


# 前端序列化器
class FrontCommentSerializer(BaseCommentsSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'article_pk', 'article_name', 'nickname', 'avatar', 'email', 'content', 'notification',
                  'parent_comment',
                  'parent_comment_nickname', 'admin_comment', 'create_time', 'reply_comments']
        # 评论深度，从参数暂定
        deep = 1
        read_only_fields = ['id', 'admin_comment', 'article_name', 'parent_comment_nickname',
                            'reply_comments',
                            'create_time']

    def create(self, validated_data):
        notification = validated_data.pop("notification", True)
        content = self.Filter.replaceSensitiveWord(validated_data.pop("content"))
        nickname = self.Filter.replaceSensitiveWord(validated_data.pop("nickname"))
        comments = Comments.objects.create(**validated_data, notification=notification, content=content,
                                           nickname=nickname)
        # 发送邮件
        if comments.parent_comment is not None and comments.parent_comment.notification:
            message = f"{comments.nickname}给您回复：{comments.content}"
            send_email(title="您在JBlog的评论收到回复啦", message=message,
                       target=comments.parent_comment.email)
        return comments


# 更新订阅状态序列化器
class SubCommentSerializer(serializers.Serializer):
    notification = serializers.BooleanField(required=True, label="是否订阅回复")

    def update(self, instance, validated_data):
        notification = validated_data.get("notification", instance.notification)
        instance.notification = notification
        instance.save()
        return instance


class CommentsTotalQueryParams(serializers.Serializer):
    article_id = serializers.IntegerField(required=True, label="文章ID")
