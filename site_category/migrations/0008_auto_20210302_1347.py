# Generated by Django 3.1.7 on 2021-03-02 13:47

from django.db import migrations
import photography_site.utilities
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('site_category', '0007_auto_20210302_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=photography_site.utilities.file_upload_name),
        ),
    ]
