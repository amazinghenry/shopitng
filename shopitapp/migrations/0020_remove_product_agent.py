# Generated by Django 3.2.5 on 2021-09-07 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0019_auto_20210902_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='agent',
        ),
    ]