from django.urls import path

from apps.posts.api.views.sighted_birds_views import SightingsByExpeditionListAPIView, BirdCreateAPIView

urlpatterns = [
    path('expeditions/<int:id>/sightings', SightingsByExpeditionListAPIView.as_view(), name = 'sightings_by_expedition'),
    path('sighted_bird', BirdCreateAPIView.as_view(), name = 'create_bird'),
    #path('sighting', SightingCreateAPIView.as_view(), name = 'sightings'),

]