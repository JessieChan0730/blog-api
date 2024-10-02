from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from blog_api.apps.common.serializer import DeleteMultiple
from .filter import CategoryFilter
from .models import Category
from .pagination import CategoryPagination
from .serializer import CategorySerializer, FrontCategorySerializer
from blog_api.apps.common.mixin import DeleteMultipleModelMixin


# Create your views here.
class CategoryViewSet(DeleteMultipleModelMixin, viewsets.ModelViewSet):
    pagination_class = CategoryPagination
    filter_backends = (DjangoFilterBackend,)
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    # 自定义过滤器
    filterset_class = CategoryFilter

    # 可以过滤的字段，默认全量匹配
    # filterset_fields = ("name",)
    def get_serializer_class(self):
        if self.action == "multiple":
            return DeleteMultiple
        return CategorySerializer

    @action(methods=['get'], detail=False)
    def all(self, request):
        all_category = self.get_queryset().all()
        serializer = self.get_serializer(all_category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.
class FrontCategoryViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.filter(display=True).all()
    permission_classes = [AllowAny]
    serializer_class = FrontCategorySerializer
