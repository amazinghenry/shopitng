# Generated by Django 3.2.8 on 2021-10-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0027_auto_20211012_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vip',
            field=models.BooleanField(default=False),
        ),
    ]
