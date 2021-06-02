from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from apps.posts.api.serializers.media_serializers import FileListSerializer, PhotoSerializer
from apps.posts.models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Photo.objects.all()
