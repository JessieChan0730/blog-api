from rest_framework import routers

from . import views

app_name = 'comments'

router = routers.DefaultRouter()
router.register(r'comments', views.AdminCommentViewSet, basename='comments')
urlpatterns = [
]

urlpatterns += router.urls
