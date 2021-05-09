from django.urls import path
from apps.users.api.api import user_api_view, user_detail_view
from apps.users.api.views.general_views import AchievementListAPIView, UserProfileView

urlpatterns = [
    path('user/', user_api_view, name = 'usuario_api'),
    path('user/<int:pk>/', user_detail_view, name = 'user_detail_api_view'),
    path('achievements/', AchievementListAPIView.as_view(), name = 'achievements'),
    
]