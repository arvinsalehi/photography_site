# Generated by Django 3.1.7 on 2021-03-01 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_category', '0002_category_visit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]