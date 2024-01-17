# Generated by Django 3.1.7 on 2021-03-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Contact Forms',
            },
        ),
    ]