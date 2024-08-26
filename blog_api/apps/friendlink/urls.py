from rest_framework import routers
from . import views

app_name = "friendlink"

router = routers.DefaultRouter()
router.register(r'link', views.FriendLinksViewSet)
urlpatterns = [
]

urlpatterns += router.urls
