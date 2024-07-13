from django.db import models


# Create your models here.
class AnnualSummary(models.Model):
    # 标题
    title = models.CharField(max_length=30, null=False, blank=False)
    # 年份
    create_year = models.IntegerField(unique=True, null=False)
    # 总结
    sum_up = models.TextField(default='今年没有总结哦')
    # 数据
    statistics_data = models.JSONField()

    class Meta:
        db_table = 'annual_summary'
