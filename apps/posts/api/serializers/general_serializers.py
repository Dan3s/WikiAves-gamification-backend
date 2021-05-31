from rest_framework import serializers

from apps.posts.models import Expedition, Bird, Sighting, Contribution




class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        exclude = ('state',)
        

class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'expedition': instance.expedition if instance.expedition is not None else '',
            'bird': instance.bird if instance.bird is not None else '',
            'creation_date': instance.creation_date,
            'is_eating': instance.is_eating,
            'is_flying': instance.is_flying,
            'is_preening': instance.is_preening,
            'is_mating': instance.is_mating,
            'is_verified': instance.is_verified
        }   

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'is_correct': instance.is_correct,
            'user': instance.user.name,
            'sightings': instance.sightings.all() if instance.sightings.all() is not None else ''
        }

class ExpeditionSerializer(serializers.ModelSerializer):
#   user = serializers.StringRelatedField()#Para mostrar el str del modelo
    #sighted_birds = SightingSerializer(many = True, source = 'sightings')

    class Meta:
        model = Expedition
        exclude = ('state',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'date': instance.date,
            'city': instance.city,
            'region': instance.region,
            'user': instance.user.name
        }
