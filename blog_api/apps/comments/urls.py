from rest_framework import routers

from . import views

app_name = 'comments'

router = routers.DefaultRouter()
router.register(r'comments', views.AdminCommentViewSet, basename='comments')
router.register(r'front/comments', views.FrontCommentViewSet, basename='front_comments')
urlpatterns = [
]

urlpatterns += router.urls
