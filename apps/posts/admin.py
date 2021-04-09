from django.contrib import admin
from apps.posts.models import Expedition, Bird, Sighting, Contribution


class ExpeditionAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'name', 'description', 'date', 'city', 'region', 'user')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'name', 'description', 'date', 'city', 'region', 'user')#Agrega la opción de buscar por estos campos

class BirdAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'name', 'specie', 'sightings')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'name', 'specie', 'sightings')#Agrega la opción de buscar por estos campos

class SightingAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'expedition', 'bird', 'creation_date', 'is_eating', 'is_flying', 'is_preening', 'is_mating', 'is_verified', 'contribution')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'expedition', 'bird', 'creation_date', 'is_eating', 'is_flying', 'is_preening', 'is_mating', 'is_verified', 'contribution')#Agrega la opción de buscar por estos campos

class ContributionAdmin(admin.ModelAdmin):#Para modificar como se muestran los registros de la tabla CLiente en el panel de admin.
    list_display=('id', 'is_correct', 'user')#Esto se hace para mostrar mas campos en el panel de administración
    search_fields=('id', 'is_correct', 'user')#Agrega la opción de buscar por estos campos

# Register your models here.
admin.site.register(Expedition, ExpeditionAdmin)
admin.site.register(Bird, BirdAdmin)
admin.site.register(Sighting, SightingAdmin)
admin.site.register(Contribution, ContributionAdmin)