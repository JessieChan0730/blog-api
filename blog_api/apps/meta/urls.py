from django.urls import path

from . import views

app_name = "meta"

urlpatterns = [
    path('meta', views.MetaApiView.as_view(), name='meta')
]
