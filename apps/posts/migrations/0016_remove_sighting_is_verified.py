# Generated by Django 3.1.7 on 2021-06-07 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20210602_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sighting',
            name='is_verified',
        ),
    ]
