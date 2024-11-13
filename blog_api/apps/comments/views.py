# Create your views here.
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from blog_api.apps.common.mixin import DeleteMultipleModelMixin
from blog_api.apps.common.serializer import DeleteMultiple
from .filter import ArticleTitleFilter
from .models import Comments
from .pagination import AdminCommentPagination, FrontCommentPagination
from .serializer import AdminCommentSerializer, SubCommentSerializer, FrontCommentSerializer, CommentsTotalQueryParams


class AdminCommentViewSet(ListModelMixin, RetrieveModelMixin, DestroyModelMixin, DeleteMultipleModelMixin,
                          GenericViewSet):
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = AdminCommentPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend,)
    filterset_class = ArticleTitleFilter

    def get_serializer_class(self):
        if self.action == "multiple":
            return DeleteMultiple
        elif self.action == "subscribe":
            return SubCommentSerializer
        return AdminCommentSerializer

    # 重新设置query_set
    def get_queryset(self):
        # 只返回 parent_comment 为 null 的顶层评论
        return Comments.objects.filter(parent_comment__isnull=True)

    @action(methods=['POST'], detail=False)
    def publish(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(methods=['PUT'], detail=True)
    def subscribe(self, request: Request, pk: int) -> Response:
        instance = self.get_queryset().get(pk=pk)
        serializer = self.get_serializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FrontCommentViewSet(ListModelMixin,
                          GenericViewSet):
    queryset = Comments.objects.all()
    permission_classes = [AllowAny]
    pagination_class = FrontCommentPagination
    # serializer_class = FrontCommentSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend,)
    filterset_class = ArticleTitleFilter

    # 重新设置query_set
    def get_queryset(self):
        # 只返回 parent_comment 为 null 的顶层评论
        return Comments.objects.filter(parent_comment__isnull=True)

    def get_serializer_class(self):
        if self.action == "total":
            return CommentsTotalQueryParams
        return FrontCommentSerializer

    @action(methods=['POST'], detail=False)
    def publish(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # 查询文章下评论总数
    @action(methods=['GET'], detail=False)
    def total(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        article_id = serializer.validated_data.get('article_id')
        total = Comments.objects.all().filter(article_pk=article_id).count()
        return Response(data={'total': total}, status=status.HTTP_200_OK)
