from article.models import Article
from django.db import models


# Create your models here.
class Comments(models.Model):
    article_pk = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, verbose_name="博客ID",
                                   related_name='comments')
    content = models.TextField(verbose_name="评论内容",max_length=255)
    avatar = models.URLField(verbose_name="头像链接")
    nickname = models.CharField(max_length=30, verbose_name="昵称")
    email = models.EmailField(verbose_name="用户接收回复的邮箱")
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies",
                                       verbose_name="评论")
    notification = models.BooleanField(default=True, verbose_name="是否接收回复通知")
    admin_comment = models.BooleanField(default=False, verbose_name="是否为作者回复")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    def __str__(self):
        return f"Comment by {self.nickname} on {self.content[:50]}..."

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"
        db_table = "comments"

    # 获取当前所有的子评论
    def get_reply_comments(self):
        return self.replies.all()  # 返回当前评论的所有子评论
