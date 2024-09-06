from typing import List

from django.db import DatabaseError
from settings.models import SettingsGroup

from .enum import RootGroupName


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


class Setting:
    def __init__(self, id, key, value, group):
        self.__key = key
        self.__value = value
        self.__group = group
        self.__id = id

    def __str_to_type(self, value: str):
        if value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        # elif value.replace(".", "", 1).isdigit():  # 简单检查是否为整数或浮点数
        #     try:
        #         return float(value)  # 尝试转换为浮点数，如果是整数，浮点数也会正常工作
        #     except ValueError:
        #         pass
        elif value.isdigit():  # 确保是纯整数
            return int(value)
        else:
            return value  # 如果不能转换为以上类型，则默认返回原字符串

    def get_id(self):
        return self.__id

    def get_key(self):
        return self.__key

    def get_value(self):
        return self.__str_to_type(self.__value)

    def get_group(self):
        return self.__group

    def format(self):
        return {
            self.__key: self.__value
        }


class Group:
    def __init__(self, id, name, father_group):
        self.__id = id
        self.__name = name
        self.__child_group = []
        self.__father_group = father_group
        self.__settings = []

    # 更新设置
    def set_settings(self, settings):
        self.__settings = settings

    # 更新设置子分组
    def set_child_group(self, child_group):
        self.__child_group = child_group

    def get_id(self) -> int:
        return self.__id

    def get_name(self) -> str:
        return self.__name

    # 获取所有设置
    def get_settings(self) -> List[Setting]:
        return self.__settings

    # 获取所有设置并且格式化为字典
    def get_settings_format(self) -> dict:
        settings = self.__settings
        settings_dict = {}
        for setting in settings:
            settings_dict[setting.get_key()] = setting.get_value()
        return settings_dict

    # 根据key查找设置
    def get_setting_by_key(self, key) -> Setting:
        settings = list(filter(lambda setting_ins: setting_ins.get_key() == key, self.__settings))
        if len(settings) == 0:
            raise DatabaseError("setting is not exists")
        return settings[0]

    # 获取所有子分组
    def get_child_group(self) -> List["Group"]:
        return self.__child_group

    # 切换到父分组
    def switch_father_group(self) -> "Group":
        return self.__father_group

    # 切换到指定子分组
    def switch_child_group(self, group_name) -> "Group":
        groups = list(filter(lambda group: group.get_name() == group_name, self.__child_group))
        if len(groups) == 0:
            raise DatabaseError("group is not exists")
        group = groups[0]
        return group


class BlogSettingsControls:
    def __init__(self, blog_settings):
        self.__blog_settings = blog_settings

    def all(self) -> List[Group]:
        return self.__blog_settings

    def format(self):
        all_settings = {}
        for group in self.__blog_settings:
            setting_dict = self.__analyze_setting_dict(group)
            all_settings[group.get_name()] = setting_dict
        return all_settings

    def __analyze_setting_dict(self, group: Group):
        format_setting = {}
        settings = group.get_settings()
        for setting in settings:
            format_setting.update({
                setting.get_key(): {
                    "id": setting.get_id(),
                    "value": setting.get_value()
                }
            })
        child_groups = group.get_child_group()
        for child_group in child_groups:
            child_format = self.__analyze_setting_dict(child_group)
            format_setting[child_group.get_name()] = child_format
        return format_setting

    def switch(self, keyword: str) -> Group:
        groups = list(
            filter(lambda group_ins: group_ins.get_name().lower() == keyword.lower(), self.__blog_settings))
        if len(groups) == 0:
            raise DatabaseError("cannot switch to a non-existing group")
        return groups.pop()

    def front(self) -> Group:
        return self.switch(RootGroupName.front_setting)

    def admin(self) -> Group:
        return self.switch(RootGroupName.admin_setting)

    def common(self) -> Group:
        return self.switch(RootGroupName.common_setting)


# @singleton
class BlogSettings:
    def __init__(self):
        self.__root_groups = SettingsGroup.objects.filter(owner=-1)
        self.__child_groups = SettingsGroup.objects.exclude(owner=-1)
        self.__blog_settings = []
        self.__controls = None

    def __analyze_setting(self, group, father_group=None):
        group_ins = Group(group.id, group.name, father_group)
        setting_ins = []
        child_groups = []
        settings = group.settings_set.all()
        for setting in settings:
            setting = Setting(id=setting.id, key=setting.key, value=setting.value, group=group_ins)
            setting_ins.append(setting)

        for child_group in self.__child_groups:
            if group.id == child_group.owner:
                child_group_ins = self.__analyze_setting(child_group, group)
                child_groups.append(child_group_ins)
                # self.__child_groups.remove(child_group)

        if len(setting_ins) > 0:
            group_ins.set_settings(setting_ins)
        if len(child_groups) > 0:
            group_ins.set_child_group(child_groups)
        return group_ins

    def __build(self):
        for group in self.__root_groups:
            group_ins = self.__analyze_setting(group)
            self.__blog_settings.append(group_ins)

    def init(self) -> BlogSettingsControls:
        if len(self.__blog_settings) == 0 and self.__controls is None:
            self.__build()
            self.__controls = BlogSettingsControls(self.__blog_settings)
        return self.__controls


@singleton
class ReadOnlyBlogSettings(BlogSettings):
    pass
