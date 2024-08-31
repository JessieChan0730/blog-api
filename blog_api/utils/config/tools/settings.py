from django.db import DatabaseError
from django.db.models import Q
from settings.models import SettingsGroup


class SettingsTools:
    def __init__(self):
        self.__groups = SettingsGroup.objects.all()
        self.__group = None
        self.__id = 0
        self.__control = Controls

    def __get_group_by_owner(self, gid: int):
        child_group = self.__groups.filter(owner=gid)
        return child_group

    def __get_group_by_name(self, name: str):
        group = self.__groups.filter(name=name).first()
        self.__group = group
        self.__id = group.id

    def front(self):
        self.__get_group_by_name("front_setting")
        return self.__control(self.__groups, self.__group, self.__id)

    def admin(self):
        self.__get_group_by_name("admin_setting")
        return self.__control(self.__groups, self.__group, self.__id)

    def common(self):
        self.__get_group_by_name("common_setting")
        return self.__control(self.__groups, self.__group, self.__id)


class Controls:

    def __init__(self, groups, group, gid):
        self.__group = group
        self.__id = gid
        self.__groups = groups

    def __str_to_type(self, value: str):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        elif value.replace(".", "", 1).isdigit():  # 简单检查是否为整数或浮点数
            try:
                return float(value)  # 尝试转换为浮点数，如果是整数，浮点数也会正常工作
            except ValueError:
                pass
        elif value.isdigit():  # 确保是纯整数
            return int(value)
        else:
            return value  # 如果不能转换为以上类型，则默认返回原字符串

    def check_group(self, group_name):
        group = self.__groups.filter(Q(owner=self.__id) & Q(name=group_name)).first()
        if group is None:
            return self
        self.__group = group
        self.__id = group.id
        return self

    def view_group(self):
        return self.__group.name

    def all(self):
        return self.__group.settings_set.all()

    def set(self, key: str, value):
        setting = self.__group.settings_set.filter(key=key).first()
        if not setting:
            return DatabaseError("setting is not exists")
        setting.value = str(value)
        setting.save()
        return self

    def find(self, key, default=None):
        setting = self.__group.settings_set.filter(key=key).first()
        if not setting:
            return default
        return self.__str_to_type(setting.value)

    def keys(self):
        settings = self.all()
        return map(lambda setting: setting.key, settings)

    def values(self):
        settings = self.all()
        return map(lambda setting: self.__str_to_type(setting.value), settings)
