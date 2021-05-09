from rest_framework import generics
from rest_framework import viewsets

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

class UserProfileView(Authentication, viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(id=self.user.id)
        return queryset