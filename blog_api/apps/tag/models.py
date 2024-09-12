from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=8,default='#409eff')

    class Meta:
        db_table = 'tags'
