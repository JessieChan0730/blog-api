from rest_framework import routers

from . import views

app_name = 'comments'

router = routers.DefaultRouter()
# TODO 是是否需要加上 article 前缀
router.register(r'comments', views.AdminCommentViewSet, basename='comments')
urlpatterns = [
]

urlpatterns += router.urls
