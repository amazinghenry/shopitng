# Generated by Django 3.2.8 on 2021-10-13 20:47

import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import BtreeGinExtension


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0028_product_vip'),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.AddIndex(
            model_name='product',
            index=django.contrib.postgres.indexes.GinIndex(
                fields=['title'], name='NewGinIndex'),
        ),
    ]