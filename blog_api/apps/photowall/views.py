from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from blog_api.apps.common.mixin import DeleteMultipleModelMixin
from blog_api.apps.common.serializer import DeleteMultiple
from .filter import PhotoWallFilter
from .models import PhotoWall
from .pagination import PhotoPagination, FrontPhotoPagination
from .serializer import PhotoWallSerializer, PhotoWallUpdateSerializer, FrontPhotoWallSerializer


# Create your views here.
class PhotoWallViewSet(DeleteMultipleModelMixin, DestroyModelMixin, CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = PhotoWall.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PhotoPagination
    filter_backends = (DjangoFilterBackend,)
    # 自定义过滤器
    filterset_class = PhotoWallFilter

    def get_serializer_class(self):
        if self.action == "change":
            return PhotoWallUpdateSerializer
        elif self.action == "multiple":
            return DeleteMultiple
        return PhotoWallSerializer

    @action(methods=['put'], detail=True)
    def change(self, request, pk=None):
        instance = self.queryset.filter(pk=pk).first()
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = self.get_serializer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# 前端请求照片墙接口
class FrontPhotoWallViewSet(ListModelMixin, GenericViewSet):
    queryset = PhotoWall.objects.filter(visible=True).all()
    permission_classes = [AllowAny]
    pagination_class = FrontPhotoPagination
    serializer_class = FrontPhotoWallSerializer
