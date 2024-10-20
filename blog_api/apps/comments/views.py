# Create your views here.
from blog_api.apps.common.mixin import DeleteMultipleModelMixin
from blog_api.apps.common.serializer import DeleteMultiple
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .filter import ArticleTitleFilter
from .models import Comments
from .pagination import AdminCommentPagination
from .serializer import AdminCommentSerializer, SubCommentSerializer


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


class FrontCommentViewSet():
    pass
