from rest_framework.routers import DefaultRouter

from apps.users.api.views.general_views import ProfileAPIView

router = DefaultRouter()

router.register(r'myprofile', ProfileAPIView, basename='myprofile')
urlpatterns = router.urls

