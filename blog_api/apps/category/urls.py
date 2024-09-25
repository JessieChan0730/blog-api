from rest_framework import routers
from . import views

app_name = "category"

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet,basename='category')
router.register(r'front/category', views.FrontCategoryViewSet,basename='front_category')
urlpatterns = [
]

urlpatterns += router.urls
