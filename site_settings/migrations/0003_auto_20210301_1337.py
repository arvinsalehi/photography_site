# Generated by Django 3.1.7 on 2021-03-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20210301_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site_setting',
            name='about_us_service',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='site_setting',
            name='about_us_title',
            field=models.CharField(max_length=256),
        ),
    ]