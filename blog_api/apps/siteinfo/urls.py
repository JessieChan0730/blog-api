from rest_framework import routers
from . import views

app_name = "siteinfo"

router = routers.DefaultRouter()
router.register(r'siteinfo', views.SiteInfoView,basename='siteinfo')
router.register(r'front/siteinfo', views.FrontSiteInfoView,basename='frontsiteinfo')
urlpatterns = [
]

urlpatterns += router.urls
