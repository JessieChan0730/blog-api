from datetime import datetime

from annual_summary.models import AnnualSummary
from rest_framework import serializers


class AnnualSummarySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30, required=True)
    sum_up = serializers.CharField(max_length=None, required=False)
    statistics_data = serializers.JSONField(required=True)
    create_year = serializers.IntegerField(read_only=True)

    # 自定义数据保存
    def create(self, validated_data):
        title = validated_data.get('title')
        sum_up = validated_data.get('sum_up')
        statistics_data = validated_data.get('statistics_data')
        year = datetime.now().year
        return AnnualSummary.objects.create(title=title, sum_up=sum_up, statistics_data=statistics_data,
                                            create_year=year)

    # 自定义数据更新
    def update(self, instance, validated_data):
        title = validated_data.get('title')
        sum_up = validated_data.get('sum_up')
        statistics_data = validated_data.get('statistics_data')
        instance.title = title
        instance.statistics_data = statistics_data
        if sum_up is not None and sum_up != '':
            instance.sum_up = sum_up
        instance.save()
        return instance
