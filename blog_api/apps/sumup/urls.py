from django.urls import path

from . import views

app_name = "sumup"

urlpatterns = [
    path('sumup/', views.StatisticsAPI.as_view(), name='all'),
]
