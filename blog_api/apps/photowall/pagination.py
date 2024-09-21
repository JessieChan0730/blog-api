from blog_api.utils.config.tools.annotation import admin_paging_setting, front_paging_setting


@admin_paging_setting(group_name="photo_wall")
class PhotoPagination:
    pass


@front_paging_setting(group_name="photo_wall")
class FrontPhotoPagination:
    pass
