from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Tag
from .pagination import TagPagination
from .serializer import TagSerializer, DeleteMultiple


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    # serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]  # 认证方式
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = TagPagination

    def get_serializer_class(self):
        if self.action == "multiple":
            return DeleteMultiple
        return TagSerializer

    # 删除多个数据
    @action(methods=['delete'], detail=False)
    def multiple(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ids = serializer.data.get('ids', [])
        Tag.objects.filter(id__in=ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
