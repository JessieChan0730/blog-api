# Generated by Django 5.0.6 on 2024-09-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteInfo",
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
                ("title", models.CharField(max_length=30, verbose_name="站点信息标题")),
                ("content", models.TextField(verbose_name="站点信息内容")),
            ],
            options={
                "db_table": "site_info",
            },
        ),
    ]
