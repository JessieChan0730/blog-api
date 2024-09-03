# 自定义分页类
from blog_api.utils.config.tools.annotation import admin_paging_setting


# 使用此分页器可以进行如下访问
# http://127.0.0.1/article/?page=1&page_size=2

# class ArticlePagination(PageNumberPagination):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.load_settings()
#
#     def load_settings(self):
#         page_size = SettingsTools().front().check_group("blog").find("page_size")
#         if page_size:
#             self.page_size = page_size
#         else:
#             self.page_size = 2
#
#     page_size_query_param = 'page_size'
#     max_page_size = 4


@admin_paging_setting(group_name="blog")
class ArticlePagination:
    pass
