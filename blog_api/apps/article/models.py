import os
import uuid

from category.models import Category
from django.contrib.auth.models import User
from django.db import models
from tag.models import Tag


# Create your models here.
class Article(models.Model):
    # 用户需要提交的
    title = models.CharField(max_length=40)
    content = models.TextField()
    intro = models.TextField(max_length=200)
    tags = models.ManyToManyField(Tag, blank=True)
    # TODO 是否可以存在一个唯一的目录
    # cover = models.ImageField(upload_to="article/cover/%Y/%m/%d")
    cover_url = models.URLField()
    recommend = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date']
        db_table = 'articles'


class ImageContent(models.Model):
    def upload_to_with_uuid(instance, filename):
        """
        为 ImageField 生成包含 UUID 的上传路径
        """
        # 生成 UUID 字符串（不带 '-'）
        uuid_str = uuid.uuid4().hex
        # 构建文件路径，例如：'article/content/UUID/filename.ext'
        # 注意：这里可以根据需要调整路径结构
        return os.path.join('article', 'content', uuid_str, filename)

    image = models.ImageField(upload_to=upload_to_with_uuid)


class Cover(models.Model):
    cover = models.ImageField(upload_to="article/cover/%Y/%m/%d")
