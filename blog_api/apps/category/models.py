from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name="分类名")
    display = models.BooleanField(default=False, verbose_name="是否展示到主页")

    class Meta:
        db_table = 'category'
