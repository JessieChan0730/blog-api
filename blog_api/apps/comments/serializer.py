from django.contrib.auth.models import User
from rest_framework import serializers
from user.models import UserDetail

from .models import Comments


class AdminCommentSerializer(serializers.ModelSerializer):
    reply_comments = serializers.SerializerMethodField()
    parent_comment_nickname = serializers.SerializerMethodField()
    article_name = serializers.SerializerMethodField()

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

    def get_reply_comments(self, obj):
        # 这里我们序列化 obj.replies.all()，即当前评论的所有子评论
        # 使用相同的 CommentSerializer，但设置 depth=1 来避免无限递归（尽管在这个例子中我们不会直接用到它）
        # 实际上，对于每个序列化器实例，我们不会直接传递 depth 参数，而是通过全局设置或视图中的配置来处理
        reply_serializers = AdminCommentSerializer(obj.replies.all(), many=True)
        return reply_serializers.data

    def get_parent_comment_nickname(self, obj):
        return obj.parent_comment.nickname if obj.parent_comment is not None else None

    def get_article_name(self, obj):
        return obj.article_pk.title if obj.article_pk is not None else ""

    def create(self, validated_data):
        # 获取当前用户详情
        user_detail = UserDetail.objects.first()
        article_pk = validated_data.get("article_pk")
        nickname = user_detail.nickname
        email = User.objects.first().email
        content = validated_data.get("content")
        notification = validated_data.get("notification", True)
        avatar = user_detail.avatar.url
        parent_comment = validated_data.get("parent_comment")
        comments = Comments.objects.create(article_pk=article_pk, nickname=nickname, content=content, avatar=avatar,
                                           parent_comment=parent_comment, admin_comment=True, notification=notification,
                                           email=email)
        return comments
