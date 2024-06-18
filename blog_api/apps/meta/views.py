from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import BlogMeta
from .serializer import MetaSerializer


# Create your views here.
class MetaApiView(APIView):
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作

    # 只有一条数据，获取第一条
    def get(self, request):
        blog_meta = BlogMeta.objects.first()
        if not blog_meta:
            raise Http404
        serializer = MetaSerializer(instance=blog_meta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        # 网站元信息只有一条，不需要用户上传pk
        blog_meta = BlogMeta.objects.first()
        serializer = MetaSerializer(data=data, instance=blog_meta)
        serializer.is_valid(raise_exception=True)
        # 更新
        serializer.save()
