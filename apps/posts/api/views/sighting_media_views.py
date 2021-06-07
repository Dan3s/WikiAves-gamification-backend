from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser, FormParser

from apps.posts.api.serializers.media_serializers import FileListSerializer, PhotoSerializer, VideoSerializer, \
    AudioSerializer
from apps.posts.models import Photo, Video, Audio
from apps.users.authentication_mixins import Authentication


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Photo.objects.all().filter(state=True)

class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Video.objects.all().filter(state=True)


class AudioViewSet(viewsets.ModelViewSet):
    serializer_class = AudioSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Audio.objects.all().filter(state=True)
