from annual_summary.models import AnnualSummary
from rest_framework import serializers


class AnnualSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualSummary
        fields = '__all__'
