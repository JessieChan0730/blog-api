from django.db import DatabaseError
from rest_framework.pagination import PageNumberPagination

from .settings import BlogSettings, ReadOnlyBlogSettings


def front_paging_setting(group_name: str):
    def proxy(cls):
        class ProxyClass(cls, PageNumberPagination):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.load_settings()

            def load_settings(self):
                group = BlogSettings().init().front().switch_child_group(group_name=group_name)
                # group = SettingsTools().front().check_group(group_name=group_name)
                if not group:
                    raise DatabaseError("group is not exists")
                self.page_size = group.get_setting_by_key("page_size").get_value()
                self.max_page_size = group.get_setting_by_key("max_page_size").get_value()
                self.page_size_query_param = 'page_size'

        return ProxyClass

    return proxy


def admin_paging_setting(group_name: str):
    def proxy(cls):
        class ProxyClass(cls, PageNumberPagination):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.load_settings()

            def load_settings(self):
                group = BlogSettings().init().admin().switch_child_group(group_name=group_name)
                # group = SettingsTools().front().check_group(group_name=group_name)
                if not group:
                    raise DatabaseError("group is not exists")
                self.page_size = group.get_setting_by_key("page_size").get_value()
                self.max_page_size = group.get_setting_by_key("max_page_size").get_value()
                self.page_size_query_param = 'page_size'

        return ProxyClass

    return proxy


def common_paging_setting(group_name: str):
    def proxy(cls):
        class ProxyClass(cls, PageNumberPagination):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.load_settings()

            def load_settings(self):
                group = BlogSettings().init().common().switch_child_group(group_name=group_name)
                # group = SettingsTools().front().check_group(group_name=group_name)
                if not group:
                    raise DatabaseError("group is not exists")
                self.page_size = group.get_setting_by_key("page_size").get_value()
                self.max_page_size = group.get_setting_by_key("max_page_size").get_value()
                self.page_size_query_param = 'page_size'

        return ProxyClass

    return proxy


def setting(path: str = None, key: str = None, is_format=False):
    def proxy(cls):
        class ProxyClass(cls):
            class Meta:
                ref_name = f'ProxyClass_{cls.__name__}'

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self._fetch_settings_later = True
                self._path = path
                self._key = key
                self._is_format = is_format

            def fetch_settings(self):
                if self._fetch_settings_later:
                    blog_setting = BlogSettings().init()
                    self.inject_setting = self.__fetch_settings_impl(blog_setting)
                    self._fetch_settings_later = False

            def __fetch_settings_impl(self, blog_setting):
                g_path = [] if path is None else path.split("/")
                if len(g_path) > 0:
                    group = blog_setting.switch(g_path.pop(0))
                    for group_name in g_path:
                        group = group.switch_child_group(group_name=group_name)
                    if key is not None:
                        return group.get_setting_by_key(key).get_value()
                    else:
                        return group.get_settings_format() if is_format else group.get_settings()
                elif key is None:
                    return blog_setting.format() if is_format else blog_setting.all()
                else:
                    raise ValueError("Passing the key parameter must pass the group parameter")

        return ProxyClass

    return proxy


def read_only_setting(path: str = None, key: str = None, is_format=False):
    def proxy(cls):
        global setting_value
        blog_setting = ReadOnlyBlogSettings().init()
        g_path = [] if path is None else path.split("/")
        if len(g_path) > 0:
            group = blog_setting.switch(g_path.pop(0))
            for group_name in g_path:
                group = group.switch_child_group(group_name=group_name)
            if key is not None:
                setting_value = group.get_setting_by_key(key).get_value()
            else:
                setting_value = group.get_settings_format() if is_format else group.get_settings()
        elif key is None:
            setting_value = blog_setting.format() if is_format else blog_setting.all()
        else:
            raise ValueError("Passing the key parameter must pass the group parameter")

        class ProxyClass(cls):
            class Meta:
                ref_name = f'ProxyClass_{cls.__name__}'
            inject_setting = setting_value

        return ProxyClass

    return proxy
