from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser, FormParser

from apps.posts.api.serializers.media_serializers import FileListSerializer, PhotoSerializer
from apps.posts.models import Photo
from apps.users.authentication_mixins import Authentication


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Photo.objects.all().filter(state=True)


