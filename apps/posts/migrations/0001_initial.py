# Generated by Django 3.1.7 on 2021-04-06 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_auto_20210406_0035'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('specie', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ave',
                'verbose_name_plural': 'Aves',
            },
        ),
        migrations.CreateModel(
            name='Expedition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripción')),
                ('date', models.DateField(verbose_name='Fecha de expedición')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('region', models.CharField(max_length=255, verbose_name='Región')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Expedición',
                'verbose_name_plural': 'Expediciones',
            },
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(verbose_name='Fecha de creación')),
                ('is_eating', models.BooleanField(default=False)),
                ('is_flying', models.BooleanField(default=False)),
                ('is_preening', models.BooleanField(default=False)),
                ('is_mating', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.bird')),
                ('contribution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.contribution')),
                ('expedition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.expedition')),
            ],
            options={
                'verbose_name': 'Avistamiento',
                'verbose_name_plural': 'Avistamientos',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='videos/', verbose_name='Videos')),
                ('sighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.sighting')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='images/', verbose_name='Fotos')),
                ('sighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.sighting')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Fotos',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='audios/', verbose_name='Audios')),
                ('sighting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.sighting')),
            ],
            options={
                'verbose_name': 'Audio',
                'verbose_name_plural': 'Audios',
            },
        ),
    ]
