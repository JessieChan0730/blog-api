from django.db import models


# Create your models here.

class SettingsGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name="分组名")
    owner = models.IntegerField(verbose_name="从属分组ID", null=True, default=-1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'settings_group'


class Settings(models.Model):
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    groupId = models.ForeignKey(SettingsGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.key

    class Meta:
        db_table = 'settings'


class FrontCover(models.Model):
    cover = models.ImageField(upload_to='setting/cover/%Y/%m/%d', verbose_name="前台封面")

    class Meta:
        db_table = 'front_cover'


class AdminLogo(models.Model):
    logo = models.ImageField(upload_to='setting/logo/%Y/%m/%d', verbose_name="后台LOGO")

    class Meta:
        db_table = 'admin_logo'
