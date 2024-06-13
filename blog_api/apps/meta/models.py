from django.db import models


# Create your models here.
class BlogMeta(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='cover')

    class Meta:
        db_table = 'blog_meta'
