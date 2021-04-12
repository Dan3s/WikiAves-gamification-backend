from rest_framework import serializers

from apps.posts.models import Expedition, Bird, Sighting, Contribution


class ExpeditionSerializer(serializers.ModelSerializer):
#   user = serializers.StringRelatedField()#Para mostrar el str del modelo
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


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        exclude = ('state',)

class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        exclude = ('state',)

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        exclude = ('state',)