# Generated by Django 5.0.6 on 2024-08-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PhotoWall",
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
                ("image", models.ImageField(upload_to="photowall/%Y/%m/%d")),
                ("description", models.CharField(max_length=255)),
                ("visible", models.BooleanField(default=True)),
            ],
        ),
    ]