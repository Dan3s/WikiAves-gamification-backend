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

    class Meta:
        model = Sighting
        # exclude = ('state',)
        fields = ['id', 'expedition', 'bird', 'date', 'is_eating', 'is_flying',
                  'is_preening', 'is_mating', 'likes', 'is_correct', 'is_verified',
                  'sighting_photos', 'sighting_videos', 'sighting_audios']

    '''def create(self, validated_data):
        photos = validated_data.pop('sighting_photos')
        videos = validated_data.pop('videos')
        audios = validated_data.pop('audios')
        sighting = Sighting.objects.create(**validated_data)

        for photo in photos:
            if photo.state:
                Sighting.objects.create(sighting=sighting, **photo)
        for video in videos:
            if video.state:
                Sighting.objects.create(sighting=sighting, **video)
        for audio in audios:
            if audio.state:
                Sighting.objects.create(sighting=sighting, **audio)

        return sighting'''

    '''def to_representation(self, instance):
        return {
            'id': instance.id,
            'expedition': instance.expedition.name if instance.expedition is not None else '',
            'bird_id': instance.bird.id,
            'bird_common_name': instance.bird.common_name,
            'bird_scientific_name': instance.bird.scientific_name,
            'bird_sightings': instance.bird.sightings,
            'date': instance.date,
            'is_eating': instance.is_eating,
            'is_flying': instance.is_flying,
            'is_preening': instance.is_preening,
            'is_mating': instance.is_mating,
            'is_verified': instance.is_verified

        }'''


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
