from rest_framework.response import Response
from rest_framework import viewsets, status, generics, filters
from rest_framework.views import APIView

from apps.posts.api.serializers.general_serializers import SightingSerializer, BirdSerializer
from apps.posts.models import Sighting
from apps.posts.utils.sighting_utils import SightingUtils
from apps.users.authentication_mixins import Authentication

CONTRIBUTION_TYPE = ['like', 'vote']


class SightingViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = SightingSerializer

    def get_queryset(self):
        # expedition_id = self.kwargs['id']
        # queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(state=True)
        return queryset


class SightingsByExpeditionListAPIView(Authentication, generics.ListAPIView):
    serializer_class = SightingSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        expedition_id = self.kwargs['expedition_id']
        queryset = self.serializer_class.Meta.model.objects.filter(expedition=expedition_id, state=True)
        return queryset


class BirdCreateAPIView(Authentication, generics.CreateAPIView):
    serializer_class = BirdSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        checker = SightingUtils()
        if serializer.is_valid():
            bird_id = checker.bird_already_exists(serializer.validated_data['scientific_name'])
            if bird_id is None:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "El ave ya existe", "bird_id": bird_id}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchBirdListAPIView(Authentication, generics.ListAPIView):
    search_fields = ['bird__common_name', 'bird__scientific_name', 'expedition__city', 'expedition__region']
    filter_backends = (filters.SearchFilter,)
    queryset = Sighting.objects.all().order_by('-date')
    serializer_class = SightingSerializer


class SightingInteractionAPIView(Authentication, APIView):

    def post(self, request, *args, **kwargs):
        # Enviar correo notificación al usuario--------------
        sighting_id = self.kwargs['sighting_id']
        interaction_type = self.kwargs['type']
        if interaction_type == CONTRIBUTION_TYPE[0]:  # like
            sighting_utils = SightingUtils()
            sighting_utils.increase_like(sighting_id)
        elif interaction_type == CONTRIBUTION_TYPE[1]:  # vote
            sighting_utils = SightingUtils()
            try:
                if request.data['vote'] or not request.data['vote']:
                    sighting_utils.create_user_vote_contribution(self.user, sighting_id, request.data['vote'])
            except:
                return Response({'message': 'El atributo del body vote debe ser true o false, booleano sin comillas'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Error en parámetro type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Interacción realizada correctamente'}, status=status.HTTP_200_OK)
