from rest_framework.pagination import PageNumberPagination


class PhotoPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = 5
    max_page_size = 5
