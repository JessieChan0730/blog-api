from django.contrib.auth.models import User
from django.db import models

from category.models import Category
from tag.models import Tag


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    intro = models.TextField()
    cover = models.ImageField(upload_to="article/%Y/%m/%d")
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_recommend = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-create_date']
        db_table = 'articles'
