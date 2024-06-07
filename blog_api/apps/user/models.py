from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# 扩展Django自带的User模型
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detail')
    signature = models.CharField(max_length=255, null=True, default="这是一条没有个性的签名")
    hobby = models.JSONField(null=True, default=[])
    avatar = models.URLField(max_length=255, null=True)
    social_contact = models.JSONField(null=True, default={})
    about_me = models.TextField()


# 利用Django信号机制来完成user detail的创建
@receiver(post_save, sender=User)
def create_user_detail(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(user=instance)
    else:
        instance.detail.save()
