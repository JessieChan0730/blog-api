from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import token_obtain_pair, token_verify, token_refresh
from .views import UserDetailViewSet, LoginOutView

app_name = "user"
router = routers.DefaultRouter()
router.register(r'user', UserDetailViewSet)

urlpatterns = [
    path('login', token_obtain_pair),  # 登录  签发token
    path('refresh', token_refresh),  # 刷新token
    path('logout', LoginOutView.as_view()),  # 删除token
]

urlpatterns += router.urls
