# Generated by Django 3.2.5 on 2021-08-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0012_auto_20210823_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
