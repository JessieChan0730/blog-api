from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog_api.utils.config.tools.annotation import setting
from blog_api.utils.config.tools.enum import RootGroupName
from .serializer import SettingSerializer


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

    def put(self, request):
        data = request.data
        serializer = SettingSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
