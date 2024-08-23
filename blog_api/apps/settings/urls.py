from django.urls import path

from . import views

app_name = "settings"

urlpatterns = [
    path('settings', views.MetaApiView.as_view(), name='settings')
]