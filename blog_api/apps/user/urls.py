
from rest_framework import routers
from .views import UserDetailViewSet, FrontUserDetailViewSet

app_name = "user"
router = routers.DefaultRouter()
router.register(r'user', UserDetailViewSet,basename='user')
router.register(r'front/user', FrontUserDetailViewSet,basename='front_user')

urlpatterns = [
]

urlpatterns += router.urls
