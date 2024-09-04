from django.urls import path

from . import views

app_name = "settings"

urlpatterns = [
    path('settings/front/', views.FrontSettingView.as_view(), name='front'),
    path('settings/admin/', views.AdminSettingView.as_view(), name='admin'),
    path('settings/', views.PutSettingsView.as_view(), name='put'),
    path('settings/front/cover/', views.FrontCoverViewSet.as_view({
        'post': 'create',
    }), name='cover'),
    path('settings/admin/logo/', views.AdminLogoViewSet.as_view({
        'post': 'create',
    }), name='logo'),
]
