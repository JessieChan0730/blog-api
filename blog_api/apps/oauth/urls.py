from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from .views import LoginOutView
app_name = "oauth"
urlpatterns = [
    path('auth/login', token_obtain_pair),  # 登录  签发token
    path('auth/refresh', token_refresh),  # 刷新token
    path('auth/logout', LoginOutView.as_view()),  # 删除token
]
