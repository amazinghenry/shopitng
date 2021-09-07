# Generated by Django 3.2.5 on 2021-08-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0011_auto_20210822_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='product_image1',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
