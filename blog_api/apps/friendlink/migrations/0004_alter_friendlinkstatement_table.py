# Generated by Django 5.0.6 on 2024-08-27 03:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("friendlink", "0003_friendlinkstatement"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="friendlinkstatement",
            table="fl_statement",
        ),
    ]
