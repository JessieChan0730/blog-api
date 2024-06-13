from django.db import models


# Create your models here.
class AnnualSummary(models.Model):
    title = models.CharField(max_length=30)
    create_year = models.IntegerField()
    sum_up = models.TextField()
    statistics_data = models.JSONField()

    class Meta:
        db_table = 'annual_summary'
