from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog_api.apps.common.mixin import DeleteMultipleModelMixin
from blog_api.apps.common.serializer import DeleteMultiple
from .models import Tag
from .pagination import TagPagination
from .serializer import TagSerializer


class TagViewSet(DeleteMultipleModelMixin, viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    # serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = TagPagination

    def get_serializer_class(self):
        if self.action == "multiple":
            return DeleteMultiple
        return TagSerializer

    @action(methods=['get'], detail=False)
    def search(self, request: Request):
        name = request.query_params.get('name', '')
        tags = self.get_queryset().filter(name__icontains=name)
        if not tags:
            return Response(data=[], status=status.HTTP_200_OK)
        serializer = self.get_serializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FrontTagViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [AllowAny]
