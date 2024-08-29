from rest_framework import routers
from . import views

app_name = "siteinfo"

router = routers.DefaultRouter()
router.register(r'siteinfo', views.SiteInfoView)
urlpatterns = [
]

urlpatterns += router.urls
