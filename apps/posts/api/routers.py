from rest_framework.routers import DefaultRouter
from apps.posts.api.views.general_views import ExpeditionViewSet, ContributionViewSet
from apps.posts.api.views.sighted_birds_views import SightingViewSet
from apps.posts.api.views.sighting_media_views import PhotoViewSet

router = DefaultRouter()

router.register(r'expeditions', ExpeditionViewSet, basename='expeditions')
#router.register(r'contributions', ContributionViewSet, basename='contributions')
router.register(r'sightings', SightingViewSet, basename='sightings')
router.register(r'photos', PhotoViewSet, basename='photos')
#router.register(r'birds', BirdViewSet, basename='birds')
urlpatterns = router.urls

