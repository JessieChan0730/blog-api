from rest_framework import routers
from . import views

app_name = "photowall"

router = routers.DefaultRouter()
router.register(r'photos', views.PhotoWallViewSet, basename='photo')
router.register(r'front/photos', views.FrontPhotoWallViewSet,basename='front_photo')
urlpatterns = [
]

urlpatterns += router.urls
