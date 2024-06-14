from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_verify, token_refresh

app_name = "user"
urlpatterns = [
    path('login', token_obtain_pair),  # 登录  签发token
    path('refresh', token_refresh),  # 刷新token
]
