from django.urls import path
#from apps.posts.api.views.general_views import ExpeditionListAPIView, ExpeditionCreatedAPIView, ContributionListAPIView, ExpeditionRetrieveAPIView, ExpeditionDestroyAPIView, ExpeditionUpdateAPIView



urlpatterns = [
    '''path('expeditions/list/', ExpeditionListAPIView.as_view(), name = 'expeditions_list'),
    path('expeditions/create/', ExpeditionCreatedAPIView.as_view(), name = 'expeditions_create'),
    path('expeditions/retrieve/<int:pk>', ExpeditionRetrieveAPIView.as_view(), name = 'expeditions_retrieve'),
    path('expeditions/destroy/<int:pk>', ExpeditionDestroyAPIView.as_view(), name = 'expeditions_destroy'),
    path('expeditions/update/<int:pk>', ExpeditionUpdateAPIView.as_view(), name = 'expeditions_update'),

    path('contributions/', ContributionListAPIView.as_view(), name = 'contributions'),
    '''
]