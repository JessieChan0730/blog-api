from django.db import models


# Create your models here.
class FriendLink(models.Model):
    STATUS_CHOICES = (
        ('pending', '审核'),
        ('on_shelf', '上架'),
        ('off_shelf', '下架'),
    )
    name = models.CharField(max_length=50, verbose_name='网站名字', blank=False)
    intro = models.CharField(max_length=120, verbose_name='网站简介', blank=False)
    link = models.URLField(verbose_name='网站链接')
    avatar = models.URLField(verbose_name='网站头像')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='pending', verbose_name='链接状态')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'friendlink'


class FriendLinkStatement(models.Model):
    statement = models.TextField()

    class Meta:
        db_table = 'fl_statement'
