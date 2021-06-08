from rest_framework.routers import DefaultRouter

from apps.users.api.views.general_views import ProfileView, UsersStatistics

router = DefaultRouter()

router.register(r'statistics', UsersStatistics, basename='users_statistics')
urlpatterns = router.urls

