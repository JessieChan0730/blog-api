from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog_api.utils.config.tools.annotation import setting
from blog_api.utils.config.tools.enum import RootGroupName
from .models import FrontCover, AdminLogo
from .serializer import SettingSerializer, AdminLogoSerializer, FrontCoverSerializer


# Create your views here.


@setting(is_format=True)
class FrontSettingView(APIView):
    def get(self, request):
        self.fetch_settings()
        settings = self.inject_setting.get(RootGroupName.front_setting)
        return Response(data=settings, status=status.HTTP_200_OK)


@setting(is_format=True)
class AdminSettingView(APIView):
    def get(self, request):
        self.fetch_settings()
        settings = self.inject_setting.get(RootGroupName.admin_setting)
        return Response(data=settings, status=status.HTTP_200_OK)


class PutSettingsView(APIView):
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作

    def put(self, request):
        data = request.data
        serializer = SettingSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


# TODO 图片上传视图是否可以封装？
class FrontCoverViewSet(CreateModelMixin, GenericViewSet):
    queryset = FrontCover.objects.all()
    serializer_class = FrontCoverSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作


class AdminLogoViewSet(CreateModelMixin, GenericViewSet):
    queryset = AdminLogo.objects.all()
    serializer_class = AdminLogoSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]
