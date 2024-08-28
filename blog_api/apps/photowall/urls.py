from rest_framework import routers
from . import views

app_name = "photowall"

router = routers.DefaultRouter()
router.register(r'photos', views.PhotoWallViewSet)
urlpatterns = [
]

urlpatterns += router.urls
