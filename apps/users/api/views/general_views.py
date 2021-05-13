from requests import Response
from rest_framework import generics, status, viewsets

from rest_framework.views import APIView

from apps.users.models import Achievement
from apps.users.api.serializers.achievement_serializers import AchievementSerializer
from apps.users.authentication_mixins import Authentication

from apps.users.models import User
from apps.users.api.serializers.user_serializers import UserSerializer

class AchievementListAPIView(generics.ListAPIView):
    serializer_class = AchievementSerializer
    
    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = Achievement.objects.filter(active=True)
        return queryset


class ProfileAPIView(Authentication, viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(id=self.user.id)
        return queryset

    def get(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(self.get_queryset())
        return Response(user_serializer.data)
