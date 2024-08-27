from rest_framework import routers
from . import views

app_name = "friendlink"

router = routers.DefaultRouter()
router.register(r'link', views.FriendLinksViewSet)
router.register(r'statement', views.FriendLinkStatementViewSet)
urlpatterns = [
]

urlpatterns += router.urls
