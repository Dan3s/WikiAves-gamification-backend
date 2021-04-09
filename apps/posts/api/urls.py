from django.urls import path
from apps.posts.api.views.general_views import ExpeditionListAPIView, ExpeditionCreatedAPIView, ContributionListAPIView

urlpatterns = [
    path('expeditions/list/', ExpeditionListAPIView.as_view(), name = 'expeditions_list'),
    path('expeditions/create/', ExpeditionCreatedAPIView.as_view(), name = 'expeditions_create'),

    path('contributions/', ContributionListAPIView.as_view(), name = 'contributions'),
    
]