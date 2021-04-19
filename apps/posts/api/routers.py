from rest_framework.routers import DefaultRouter
from apps.posts.api.views.general_views import ExpeditionViewSet, ContributionViewSet, BirdViewSet, SightingViewSet

router = DefaultRouter()

router.register(r'expeditions', ExpeditionViewSet, basename='expeditions')
router.register(r'contributions', ContributionViewSet, basename='contributions')
router.register(r'sightings', SightingViewSet, basename='sightins')
router.register(r'birds', BirdViewSet, basename='birds')
urlpatterns = router.urls

