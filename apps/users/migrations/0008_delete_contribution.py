# Generated by Django 3.1.7 on 2021-04-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210409_0139'),
        ('users', '0007_auto_20210406_0112'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contribution',
        ),
    ]
