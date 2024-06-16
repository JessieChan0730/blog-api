from rest_framework import routers
from . import views

app_name = "user"

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)
urlpatterns = [
]

urlpatterns += router.urls
