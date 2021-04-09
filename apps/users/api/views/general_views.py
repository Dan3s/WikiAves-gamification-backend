from rest_framework import generics

from apps.users.models import Achievement
from apps.users.api.serializers.achievement_serializers import AchievementSerializer

class AchievementListAPIView(generics.ListAPIView):
    serializer_class = AchievementSerializer
    
    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = Achievement.objects.filter(active=True)
        return queryset