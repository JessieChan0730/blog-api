from django.conf import settings
from django.db import models


# Create your models here.
class BlogSettings(models.Model):
    # 网页标题
    title = models.CharField(max_length=25)
    # blog封面
    cover = models.ImageField(upload_to='cover/%Y/%m/%d')

    class Meta:
        db_table = 'blog_settings'
