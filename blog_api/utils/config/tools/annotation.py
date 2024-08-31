from django.db import DatabaseError
from rest_framework.pagination import PageNumberPagination

from .settings import SettingsTools


def front_paging_setting(group_name: str):
    def proxy(cls):
        class ProxyClass(cls, PageNumberPagination):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.load_settings()

            def load_settings(self):
                group = SettingsTools().front().check_group(group_name=group_name)
                if not group:
                    raise DatabaseError("group is not exists")
                self.page_size = group.find("page_size", 2)
                self.max_page_size = group.find("max_page_size", 4)
                self.page_size_query_param = 'page_size'

        return ProxyClass

    return proxy


def admin_paging_setting(group_name: str):
    def proxy(cls):
        class ProxyClass(cls, PageNumberPagination):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.load_settings()

            def load_settings(self):
                group = SettingsTools().admin().check_group(group_name=group_name)
                if not group:
                    raise DatabaseError("group is not exists")
                self.page_size = group.find("page_size", 2)
                self.max_page_size = group.find("max_page_size", 4)
                self.page_size_query_param = 'page_size'

        return ProxyClass

    return proxy


def common_paging_setting(group_name: str):
    def proxy(cls):
        class ProxyClass(cls, PageNumberPagination):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.load_settings()

            def load_settings(self):
                group = SettingsTools().common().check_group(group_name=group_name)
                if not group:
                    raise DatabaseError("group is not exists")
                self.page_size = group.find("page_size", 2)
                self.max_page_size = group.find("max_page_size", 4)
                self.page_size_query_param = 'page_size'

        return ProxyClass

    return proxy


def setting(prop: str):
    def proxy(cls):
        class ProxyClass(cls, PageNumberPagination):
            setting = prop

        return ProxyClass

    return proxy
