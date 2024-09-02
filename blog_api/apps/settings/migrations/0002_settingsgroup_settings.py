# Generated by Django 5.0.6 on 2024-08-30 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SettingsGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="分组名")),
                ("owner", models.IntegerField(verbose_name="从属分组ID")),
            ],
            options={
                "db_table": "settings_group",
            },
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=255)),
                ("value", models.CharField(max_length=255)),
                (
                    "groupId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="settings.settingsgroup",
                    ),
                ),
            ],
            options={
                "db_table": "settings",
            },
        ),
    ]