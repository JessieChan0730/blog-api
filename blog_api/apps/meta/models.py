from django.db import models


# Create your models here.
class BlogMeta(models.Model):
    # 网页标题
    title = models.CharField(max_length=255)
    # blog封面
    cover = models.ImageField(upload_to='cover')

    class Meta:
        db_table = 'blog_meta'
