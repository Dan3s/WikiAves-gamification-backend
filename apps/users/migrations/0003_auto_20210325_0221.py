# Generated by Django 3.1.7 on 2021-03-25 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210324_0201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='image',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='image',
            new_name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='historicaluser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='city',
            field=models.CharField(default='', max_length=255, verbose_name='Ciudad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='last_names',
            field=models.CharField(default='', max_length=255, verbose_name='Apellidos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='pages_visited',
            field=models.IntegerField(default=0, verbose_name='Páginas visitadas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='region',
            field=models.CharField(default='', max_length=255, verbose_name='Región'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='xp',
            field=models.IntegerField(default=0, verbose_name='Experiencia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=255, verbose_name='Ciudad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_names',
            field=models.CharField(default='', max_length=255, verbose_name='Apellidos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='pages_visited',
            field=models.IntegerField(default=0, verbose_name='Páginas visitadas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(default='', max_length=255, verbose_name='Región'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='xp',
            field=models.IntegerField(default=0, verbose_name='Experiencia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Nombres'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='username',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Nombre de usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Nombres'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario'),
        ),
    ]
