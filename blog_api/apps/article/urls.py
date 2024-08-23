from rest_framework import routers
from . import views

app_name = "article"

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'image', views.ImageUploadViewSet)
router.register(r'cover', views.CoverViewSet)
urlpatterns = [
]

urlpatterns += router.urls
