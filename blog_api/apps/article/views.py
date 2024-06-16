from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from article.models import Article

from article.serializers import ArticleSerializer


# Create your views here.

class ArticleViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作

    @action(methods=['POST'], detail=False)
    def publish(self, request: Request) -> Response:
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 传递额外的数据
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def change(self, request: Request, pk):
        article = Article.objects.filter(pk=pk).first()
        data = request.data
        serializer = self.get_serializer(data=data, instance=article, partial=True)
        serializer.is_valid(raise_exception=True)

        if not article:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'message': '文章不存在'
            })
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
