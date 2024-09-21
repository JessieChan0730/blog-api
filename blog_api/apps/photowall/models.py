from django.db import models


# Create your models here.
class PhotoWall(models.Model):
    image = models.ImageField(upload_to='photowall/%Y/%m/%d', verbose_name="图片")
    description = models.CharField(max_length=255, verbose_name="图片介绍")
    visible = models.BooleanField(default=True, verbose_name="是否可见")

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'photowall'
