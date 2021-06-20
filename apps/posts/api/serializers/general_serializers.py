from rest_framework import serializers

from apps.posts.api.serializers.media_serializers import VideoSerializer, AudioSerializer, PhotoSerializer
from apps.posts.models import Expedition, Bird, Sighting, Contribution


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        exclude = ('state',)


class SightingSerializer(serializers.ModelSerializer):
    sighting_photos = PhotoSerializer(many=True, read_only=True)
    sighting_videos = VideoSerializer(many=True, read_only=True)
    sighting_audios = AudioSerializer(many=True, read_only=True)
    bird = BirdSerializer(read_only=True)
    bird_id = serializers.PrimaryKeyRelatedField(source='bird', queryset=Bird.objects.all(), write_only=True)

    class Meta:
        model = Sighting
        # exclude = ('state',)
        fields = ['id', 'expedition', 'bird', 'bird_id', 'date', 'is_eating', 'is_flying',
                  'is_preening', 'is_mating', 'likes', 'is_correct', 'is_verified',
                  'sighting_photos', 'sighting_videos', 'sighting_audios']


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
