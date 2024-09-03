from rest_framework.pagination import PageNumberPagination

from blog_api.utils.config.tools.annotation import admin_paging_setting


@admin_paging_setting(group_name="category")
class CategoryPagination:
    pass
