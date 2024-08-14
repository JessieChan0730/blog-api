from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog_api.utils.result.format import render_data
from .models import Article
from .pagination import ArticlePagination
from .serializers import ArticleSerializer


# Create your views here.

class ArticleViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]  # 权限类，匿名用户只读，登录用户可以操作
    pagination_class = ArticlePagination

    # 发表
    @action(methods=['POST'], detail=False)
    def publish(self, request: Request) -> Response:
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        # 传递额外的数据
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 更新
    @action(methods=['POST'], detail=True)
    def change(self, request: Request, pk) -> Response:
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

    # 获取推荐文章
    @action(methods=['GET'], detail=False)
    def recommend(self, request: Request) -> Response:
        comm_article = Article.objects.filter(is_recommend=True)
        serializer = self.get_serializer(instance=comm_article, many=True)
        return Response(data=render_data(code=200, msg="获取文章列表成功", data=serializer.data), status=status.HTTP_200_OK)

    # 分类文章
    @action(methods=['GET'], detail=False)
    def category(self, request: Request) -> Response:
        # query参数
        category_id = request.query_params.get('category_id', None)
        if category_id is None:
            return Response(data={
                'message': '请传递分类ID'
            }, status=status.HTTP_400_BAD_REQUEST)
        articles = Article.objects.filter(category_id=category_id)
        serializer = self.get_serializer(instance=articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
