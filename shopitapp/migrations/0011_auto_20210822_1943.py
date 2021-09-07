# Generated by Django 3.2.5 on 2021-08-22 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0010_auto_20210822_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopitapp.ram'),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopitapp.storage'),
        ),
    ]