from abc import ABC

from rest_framework import serializers

from apps.posts.models import Sighting, Photo


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        read_only_fields = ("sighting",)
        exclude = ('state',)

    file = serializers.ListField(
        child=serializers.FileField(max_length=100000,
                                    allow_empty_file=False,
                                    use_url=False)
    )

    def create(self, validated_data):
        sighting_id = validated_data['sighting']
        print(sighting_id)
        sighting = Sighting.objects.filter(sighting=sighting_id).first()
        file = validated_data.pop('file')
        for media in file:
            photo = Photo.objects.create(file=file, sighting=sighting, **validated_data)
        return photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        #read_only_fields = ("sighting",)
        exclude = ('state',)
