from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .filter import FriendLinkFilter
from .models import FriendLink, FriendLinkStatement
from .pagination import FriendLinkPagination
from .serializer import FriendLinkSerializer, FriendLinkStatementSerializer, FrontFriendLinkSerializer
from blog_api.apps.common.serializer import DeleteMultiple
from blog_api.apps.common.mixin import DeleteMultipleModelMixin


# Create your views here.
class FriendLinksViewSet(DeleteMultipleModelMixin,ListModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet):
    queryset = FriendLink.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = FriendLinkPagination
    filter_backends = (DjangoFilterBackend,)
    # 自定义过滤器
    filterset_class = FriendLinkFilter

    def get_serializer_class(self):
        if self.action == "multiple":
            return DeleteMultiple
        return FriendLinkSerializer


class FriendLinkStatementViewSet(GenericViewSet):
    queryset = FriendLinkStatement.objects.all()
    serializer_class = FriendLinkStatementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(methods=['get'], detail=False)
    def show(self, request):
        statement_ins = self.queryset.first()
        if not statement_ins:
            raise APIException("友链页面信息不存在")
        serializer = self.get_serializer(instance=statement_ins)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False)
    def change(self, request):
        data = request.data
        statement_ins = self.queryset.first()
        if not statement_ins:
            raise APIException("友链页面信息不存在")
        serializer = self.get_serializer(instance=statement_ins, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# 前端接口
class FrontFriendLinksViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = FriendLink.objects.filter(status='on_shelf').all()
    permission_classes = [AllowAny]
    serializer_class = FrontFriendLinkSerializer


class FrontFriendLinkStatementViewSet(GenericViewSet):
    queryset = FriendLinkStatement.objects.all()
    serializer_class = FriendLinkStatementSerializer
    permission_classes = [AllowAny]

    @action(methods=['get'], detail=False)
    def show(self, request):
        statement_ins = self.queryset.first()
        if not statement_ins:
            raise APIException("友链页面信息不存在")
        serializer = self.get_serializer(instance=statement_ins)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
