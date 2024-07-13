from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# 扩展Django自带的User模型
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detail')
    signature = models.CharField(max_length=255, null=True, default="这是一条没有个性的签名")
    # 爱好
    # JSON格式如下 [ { 'img':'icon','title':'标题','content':'内容' } ]
    hobby = models.JSONField(null=True, default=dict)
    avatar = models.URLField(null=True)
    # 社交链接
    # JSON格式如下 { ‘github’:'https://github.io.com' }
    social_contact = models.JSONField(null=True, default=dict)
    about_me = models.TextField()


# 利用Django信号机制来完成user detail的创建
@receiver(post_save, sender=User)
def create_user_detail(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)
    else:
        instance.detail.save()
