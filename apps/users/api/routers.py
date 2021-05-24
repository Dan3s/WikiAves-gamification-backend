from rest_framework.routers import DefaultRouter

from apps.users.api.views.general_views import ProfileView

router = DefaultRouter()

#router.register(r'myprofile', ProfileView, basename='myprofile')
urlpatterns = router.urls

