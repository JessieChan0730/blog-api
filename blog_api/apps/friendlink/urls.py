from rest_framework import routers
from . import views

app_name = "friendlink"

router = routers.DefaultRouter()
router.register(r'link', views.FriendLinksViewSet,basename='link')
router.register(r'front/link', views.FrontFriendLinksViewSet,basename='front_link')
router.register(r'statement', views.FriendLinkStatementViewSet,basename='statement_link')
router.register(r'front/statement', views.FriendLinkStatementViewSet,basename='statement_front_link')
urlpatterns = [
]

urlpatterns += router.urls
