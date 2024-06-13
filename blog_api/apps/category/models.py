from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'category'
