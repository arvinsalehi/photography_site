# Generated by Django 3.1.7 on 2021-03-05 12:32

from django.db import migrations, models
import photography_site.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('site_category', '0009_auto_20210302_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to=photography_site.utilities.file_upload_name),
        ),
    ]
