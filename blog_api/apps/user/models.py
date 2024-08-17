from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# 扩展Django自带的User模型
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='detail')
    nickname = models.CharField(max_length=15)
    signature = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
    about_me = models.TextField()
    more_info = models.JSONField(default=dict)

    class Meta:
        db_table = 'user_detail'


# 利用Django信号机制来完成user detail的创建
@receiver(post_save, sender=User)
def create_user_detail(sender, instance, created, **kwargs):
    if created:
        manager_info: dict = settings.MANAGER_SETTINGS
        user_detail = UserDetail()
        user_detail.user = instance
        user_detail.nickname = manager_info.get('nickname', '')
        user_detail.signature = manager_info.get('signature', '')
        user_detail.about_me = manager_info.get('about_me', '')
        hobby = manager_info.get("hobby")
        media = manager_info.get("media")
        more_info = {
            "hobby": hobby,
            "media": media,
        }
        user_detail.more_info = more_info
        user_detail.save()
    else:
        instance.detail.save()
