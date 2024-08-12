from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets

from .filter import CategoryFilter
from .models import Category
from .pagination import CategoryPagination
from .serializer import CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    filter_backends = (DjangoFilterBackend,)
    queryset = Category.objects.all()
    # 自定义过滤器
    filterset_class = CategoryFilter
    # 可以过滤的字段，默认全量匹配
    # filterset_fields = ("name",)
