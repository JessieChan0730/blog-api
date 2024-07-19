from django.urls import path

from .views import AnnualSummaryViewSet

urlpatterns = [
    path('annual', AnnualSummaryViewSet.as_view({'post': 'create', 'get': 'list'})),
    # re_path('annual/(?P<year>\d{4})', AnnualSummaryViewSet.as_view({'get': 'look'})),
    path('annual/<int:year>', AnnualSummaryViewSet.as_view({'get': 'look', 'put': 'update'}))
]
