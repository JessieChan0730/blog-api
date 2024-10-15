from rest_framework import routers

from . import views

app_name = "article"

router = routers.DefaultRouter()
# TODO 是是否需要加上 article 前缀
router.register(r'article', views.ArticleViewSet, basename='article')
router.register(r'image', views.ImageUploadViewSet)
router.register(r'cover', views.CoverViewSet)
router.register(r'front/article', views.FrontArticleViewSet, basename='front_article')
urlpatterns = [
]

urlpatterns += router.urls
