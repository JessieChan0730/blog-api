from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import token_obtain_pair, token_verify, token_refresh
from .views import UserDetailViewSet

app_name = "user"
router = routers.DefaultRouter()
router.register(r'user', UserDetailViewSet)

urlpatterns = [
]

urlpatterns += router.urls
