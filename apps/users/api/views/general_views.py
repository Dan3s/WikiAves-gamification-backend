from requests import Response
from rest_framework import generics, status, viewsets
from rest_framework.generics import RetrieveAPIView

from rest_framework.views import APIView

from apps.users.models import Achievement
from apps.users.api.serializers.achievement_serializers import AchievementSerializer, UserAchievementSerializer
from apps.users.api.serializers.user_serializers import UserSerializer, UserRankingSerializer, UserProfileSerializer
from apps.users.authentication_mixins import Authentication

class AchievementListAPIView(Authentication, generics.ListAPIView):
    serializer_class = AchievementSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        queryset = Achievement.objects.all()
        return queryset


class ProfileView(Authentication, generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = self.serializer_class.Meta.model.objects.filter(id=user_id)

        obj = queryset.get()
        return queryset


class UserAchievementsListAPIView(Authentication, generics.ListAPIView):
    serializer_class = UserAchievementSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        user_id = self.kwargs['pk']
        queryset = self.serializer_class.Meta.model.objects.filter(user=user_id)
        return queryset

class UserRankingListAPIView(Authentication, generics.ListAPIView):
    serializer_class = UserRankingSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.all().order_by('-xp')
        return queryset

class UserRankingByRegionListAPIView(Authentication, generics.ListAPIView):
    serializer_class = UserRankingSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        region = self.kwargs['region']
        queryset = self.serializer_class.Meta.model.objects.filter(region=region).order_by('-xp')
        return queryset
