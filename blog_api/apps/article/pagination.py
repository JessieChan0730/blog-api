# 自定义分页类
from rest_framework.pagination import PageNumberPagination


# 使用此分页器可以进行如下访问
# http://127.0.0.1/article/?page=1&page_size=2
class ArticlePagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 2
    max_page_size = 4
