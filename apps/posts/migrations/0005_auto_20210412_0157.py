# Generated by Django 3.1.7 on 2021-04-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210409_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bird',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contribution',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expedition',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sighting',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.BooleanField(default=True),
        ),
    ]
