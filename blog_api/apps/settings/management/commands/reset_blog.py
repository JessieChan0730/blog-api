from django.conf import settings
from django.core.management.base import BaseCommand
from settings.models import SettingsGroup, Settings


class Command(BaseCommand):
    help = 'clear blog settings'

    def handle(self, *args, **options):
        SettingsGroup.objects.all().delete()