from django.db import models
from apps.users.models import User
# Create your models here.


class Bird(models.Model):
    """Model definition for Bird."""

    # TODO: Define fields here
    id = models.AutoField(primary_key= True)
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    sightings = models.IntegerField(default=0, blank=True)
    state = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Bird."""

        verbose_name = 'Ave'
        verbose_name_plural = 'Aves'

    def __str__(self):
        """Unicode representation of Photo."""
        return self.scientific_name

class Expedition(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField('Nombre', max_length = 255, null=False, blank = False)
    description = models.CharField('Descripción', max_length = 255, null=True, blank = True)
    date = models.DateField('Fecha de expedición', null=False, blank = False)
    city = models.CharField('Ciudad',max_length = 255, null=False, blank = False)
    region = models.CharField('Región',max_length = 255, null=False, blank = False)
    state = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sighted_birds = models.ManyToManyField(Bird, through='Sighting', related_name='pepe')
    

    class Meta:
        verbose_name = 'Expedición'
        verbose_name_plural = 'Expediciones'

    def __str__(self):
        """Unicode representation of Photo."""
        return self.name


class Sighting(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    id = models.AutoField(primary_key= True)
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    date = models.DateField('Fecha de creación', null=False, blank = False)
    is_eating = models.BooleanField(default=False)
    is_flying = models.BooleanField(default=False)
    is_preening = models.BooleanField(default=False)
    is_mating = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=None, null=True, blank=True)
    likes = models.IntegerField(default=0, blank=True)
    is_verified = models.BooleanField(default=False, blank=True)
    state = models.BooleanField(default=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Avistamiento'
        verbose_name_plural = 'Avistamientos'

    def __str__(self):
        """Unicode representation of Photo."""
        return self.expedition.name


class Contribution(models.Model):
    id = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sightings = models.ManyToManyField(Sighting)
    vote = models.BooleanField(default=None, null=True, blank=True)
    state = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contribución'
        verbose_name_plural = 'Contribuciones'
        
class Photo(models.Model):
    """Model definition for Photo."""

    # TODO: Define fields here
    id = models.AutoField(primary_key= True)
    file= models.ImageField(upload_to='photos/', null=False, verbose_name="Fotos")
    state = models.BooleanField(default=True, blank=True)
    sighting = models.ForeignKey(Sighting, related_name='sighting_photos', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Photo."""

        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        """Unicode representation of Photo."""
        pass

class Video(models.Model):
    """Model definition for Video."""

    # TODO: Define fields here
    id = models.AutoField(primary_key= True)
    file = models.FileField(upload_to='videos/', null=True, verbose_name="Videos")
    state = models.BooleanField(default=True, blank=True)
    sighting = models.ForeignKey(Sighting, related_name='sighting_videos', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Video."""

        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        """Unicode representation of Videos."""
        pass

class Audio(models.Model):
    """Model definition for Audio."""

    # TODO: Define fields here
    id = models.AutoField(primary_key= True)
    file = models.FileField(upload_to='audios/', null=True, verbose_name="Audios")
    state = models.BooleanField(default=True, blank=True)
    sighting = models.ForeignKey(Sighting, related_name='sighting_audios', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Audio."""

        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'

    def __str__(self):
        """Unicode representation of Audio."""
        pass