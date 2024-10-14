from article.models import Article
from django.db import models


# Create your models here.
class Comments(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, null=False, verbose_name="博客ID",
                                   related_name='comments')
    content = models.TextField(verbose_name="评论内容")
    avatar = models.URLField(verbose_name="头像链接")
    nickname = models.CharField(max_length=255, verbose_name="昵称")
    parent_comment = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="replies",
                                       verbose_name="评论")
    admin_comment = models.BooleanField(default=False, verbose_name="是否为作者回复")
    createTime = models.DateTimeField(auto_now_add=True,verbose_name="评论时间")

    def __str__(self):
        return f"Comment by {self.nickname} on {self.content[:50]}..."

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论"

    # 获取当前所有的子评论
    def get_reply_comments(self):
        return self.replies.all()  # 返回当前评论的所有子评论
