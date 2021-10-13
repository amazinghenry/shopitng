# Generated by Django 3.2.8 on 2021-10-12 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopitapp', '0025_auto_20211011_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='display',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shopitapp.display'),
        ),
    ]
