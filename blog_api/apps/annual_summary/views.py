from annual_summary.models import AnnualSummary
from annual_summary.serializer import AnnualSummarySerializer
from rest_framework.generics import GenericAPIView


# Create your views here.
class AnnualSummaryViewSet(GenericAPIView):
    serializer_class = AnnualSummarySerializer
    queryset = AnnualSummary.objects.all()
