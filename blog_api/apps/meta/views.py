from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import APIException
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
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: MetaSerializer()}
    )
    def get(self, request):
        blog_meta = BlogMeta.objects.first()
        if not blog_meta:
            raise APIException("博客信息不存在")
        serializer = MetaSerializer(instance=blog_meta)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=MetaSerializer(),
        responses={status.HTTP_200_OK: MetaSerializer()}
    )
    def post(self, request):
        data = request.data
        # 网站元信息只有一条，不需要用户上传pk
        serializer = MetaSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 更新
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
