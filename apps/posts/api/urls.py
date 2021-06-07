from django.urls import path

from apps.posts.api.views.sighted_birds_views import SightingsByExpeditionListAPIView, BirdCreateAPIView, \
    SearchBirdListAPIView, SightingInteractionAPIView

urlpatterns = [
    path('expeditions/<int:expedition_id>/sightings', SightingsByExpeditionListAPIView.as_view(), name = 'sightings_by_expedition'),
    path('bird', BirdCreateAPIView.as_view(), name = 'create_bird'),
    path('birds', SearchBirdListAPIView.as_view(), name = 'search_bird'),
    path('sighting/<int:sighting_id>/interaction/<str:type>', SightingInteractionAPIView.as_view(), name = 'sighting_interaction'),
    #path('sighting', SightingCreateAPIView.as_view(), name = 'sightings'),

]