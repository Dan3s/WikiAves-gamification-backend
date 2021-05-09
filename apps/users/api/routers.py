from rest_framework.routers import DefaultRouter
from apps.users.api.views.general_views import UserProfileView

router = DefaultRouter()

router.register(r'myprofile', UserProfileView, basename='myprofile')
urlpatterns = router.urls

