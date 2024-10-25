# 自定义分页类
from blog_api.utils.config.tools.annotation import admin_paging_setting, front_paging_setting


@admin_paging_setting(group_name="comments")
class AdminCommentPagination:
    pass


@front_paging_setting(group_name="comments")
class FrontCommentPagination:
    pass
