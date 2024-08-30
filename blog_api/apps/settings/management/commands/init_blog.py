from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction, DatabaseError
from settings.models import SettingsGroup, Settings


class Command(BaseCommand):
    help = 'init blog settings'

    def save_settings_group(self, name: str, owner: int):
        settings_group = SettingsGroup.objects.create(name=name, owner=owner)
        return settings_group

    def save_settings(self, key, value, groupId):
        settings_ins = Settings.objects.create(key=key, value=value, groupId=groupId)
        return settings_ins

    @transaction.atomic
    def analyze_setting(self, blog_setting: dict, group=None):
        for key, value in blog_setting.items():
            if isinstance(value, dict):
                group_id = -1 if not group else group.id
                settings_group = self.save_settings_group(name=key.lower(), owner=group_id)
                self.analyze_setting(blog_setting=value, group=settings_group)
            else:
                if value is None:
                    raise DatabaseError("The settings value cannot be None")
                if not group:
                    raise DatabaseError("The blog setting file has an error, please check it")
                if value and not isinstance(value, str):
                    value = str(value)
                self.save_settings(key=key.lower(), value=value, groupId=group)

    def handle(self, *args, **options):
        self.analyze_setting(settings.BLOG_SETTINGS)
