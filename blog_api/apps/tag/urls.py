from rest_framework import routers
from . import views

app_name = "tag"

router = routers.DefaultRouter()
router.register(r'tag', views.TagViewSet,basename='tag')
router.register(r'front/tag', views.FrontTagViewSet,basename='front_tag')
urlpatterns = [
]

urlpatterns += router.urls
