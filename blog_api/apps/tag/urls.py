from rest_framework import routers
from . import views

app_name = "tag"

router = routers.DefaultRouter()
router.register(r'tag', views.TagViewSet)
urlpatterns = [
]

urlpatterns += router.urls
