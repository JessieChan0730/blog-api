# Generated by Django 5.0.6 on 2024-08-29 03:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdetail",
            name="about_me",
        ),
    ]