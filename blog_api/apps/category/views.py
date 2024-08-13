from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .filter import CategoryFilter
from .models import Category
from .pagination import CategoryPagination
from .serializer import CategorySerializer, DeleteMultiple


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    # serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = (DjangoFilterBackend,)
    queryset = Category.objects.all()
    # 自定义过滤器
    filterset_class = CategoryFilter

    # 可以过滤的字段，默认全量匹配
    # filterset_fields = ("name",)
    def get_serializer_class(self):
        if self.action == "multiple":
            return DeleteMultiple
        return CategorySerializer

    # 删除多个数据
    @action(methods=['delete'], detail=False)
    def multiple(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ids = serializer.data.get('ids', [])
        Category.objects.filter(id__in=ids).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
