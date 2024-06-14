from rest_framework import routers
from . import views

app_name = "category"

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
urlpatterns = [
]

urlpatterns += router.urls
