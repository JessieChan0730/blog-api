# Generated by Django 5.0.6 on 2024-06-07 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserDetail",
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
                (
                    "signature",
                    models.CharField(default="这是一条没有个性的签名", max_length=255, null=True),
                ),
                ("hobby", models.JSONField(default=[], null=True)),
                ("avatar", models.URLField(max_length=255, null=True)),
                ("social_contact", models.JSONField(default={}, null=True)),
                ("about_me", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="detail",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]