# Generated by Django 3.1.7 on 2021-03-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_photo', '0005_photo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(default='', max_length=30, null=True),
        ),
    ]
