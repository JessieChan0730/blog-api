from django.db import models


# Create your models here.
class SiteInfo(models.Model):
    title = models.CharField(max_length=30, verbose_name="站点信息标题")
    content = models.TextField(verbose_name="站点信息内容")

    class Meta:
        db_table = 'site_info'
