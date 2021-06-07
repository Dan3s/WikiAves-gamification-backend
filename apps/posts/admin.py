from django.contrib import admin
from apps.posts.models import Expedition, Bird, Sighting, Contribution, Photo, Video, Audio


class ExpeditionAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'name', 'description', 'date', 'city', 'region', 'user')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'name', 'description', 'date', 'city', 'region', 'user')#Agrega la opción de buscar por estos campos

class BirdAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'common_name', 'scientific_name', 'sightings')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'common_name', 'scientific_name', 'sightings')#Agrega la opción de buscar por estos campos

class SightingAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'expedition', 'bird', 'date', 'is_eating', 'is_flying', 'is_preening', 'is_mating')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'expedition', 'bird', 'date', 'is_eating', 'is_flying', 'is_preening', 'is_mating')#Agrega la opción de buscar por estos campos

class ContributionAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'user', 'vote')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'user', 'vote')#Agrega la opción de buscar por estos campos

class PhotoAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'file', 'sighting')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'file', 'sighting')#Agrega la opción de buscar por estos campos

class VideoAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'file', 'sighting')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'file', 'sighting')#Agrega la opción de buscar por estos campos

class AudioAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'file', 'sighting')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'file', 'sighting')#Agrega la opción de buscar por estos campos


# Register your models here.
admin.site.register(Expedition, ExpeditionAdmin)
admin.site.register(Bird, BirdAdmin)
admin.site.register(Sighting, SightingAdmin)
admin.site.register(Contribution, ContributionAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)