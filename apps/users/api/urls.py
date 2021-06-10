from django.urls import path
from apps.users.api.api import user_api_view, user_detail_view
from apps.users.api.views.general_views import AchievementListAPIView, ProfileView, UserAchievementsListAPIView, \
    UserRankingListAPIView, UserRankingByRegionListAPIView, RequestPasswordResetEmailGenericAPIView, \
    PasswordTokenCheckGenericAPIView, SetNewPasswordGenericAPIView

urlpatterns = [
    path('user', user_api_view, name = 'usuario_api'),
    path('user/<int:pk>', user_detail_view, name = 'user_detail_api_view'),
    path('achievements', AchievementListAPIView.as_view(), name = 'achievements'),
    path('<int:pk>/profile', ProfileView.as_view(), name='user_profile'),
    path('<int:pk>/achievements', UserAchievementsListAPIView.as_view(), name='user_achievements'),
    path('ranking', UserRankingListAPIView.as_view(), name='ranking'),
    path('ranking/<str:region>', UserRankingByRegionListAPIView.as_view(), name='ranking_by_region'),
    path('request-reset-email', RequestPasswordResetEmailGenericAPIView.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>', PasswordTokenCheckGenericAPIView.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordGenericAPIView.as_view(), name='password-reset-complete'),

    ]