"""
URL configuration for blog_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API接口文档平台",  # 必传
        default_version='v0.1',  # 必传
        description="博客系统API接口文档",
        terms_of_service="http://api.xiaogongjin.site",  # 服务条款
        contact=openapi.Contact(email="2403428097@qq.com"),
        license=openapi.License(name="BSD License"),  # 许可证
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # 权限类
)

urlpatterns = [
                  # 接口文档地址
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                          schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
                       name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schemaredoc'),
                  # api接口地址
                  path('admin', admin.site.urls),
                  path('api/', include("user.urls")),
                  path('api/', include("article.urls")),
                  path('api/', include("tag.urls")),
                  path('api/', include("category.urls")),
                  path('api/', include("settings.urls")),
                  path('api/', include("annual_summary.urls")),
                  path('api/', include("friendlink.urls")),
                  path('api/', include("photowall.urls")),
                  path('api/', include("siteinfo.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
