# Generated by Django 3.2.5 on 2021-08-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0015_alter_product_product_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]