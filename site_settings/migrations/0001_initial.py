# Generated by Django 3.1.7 on 2021-03-01 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site_Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=256)),
                ('about_us', models.TextField()),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
                ('tel_phone', models.CharField(max_length=8)),
            ],
        ),
    ]
