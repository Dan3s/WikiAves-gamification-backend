from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.posts.utils.achievement_utils import AchievementsCheckers

#from apps.posts.models import Expedition, Bird, Sighting
from apps.posts.utils.user_xp_utils import UserXpUtils
from apps.users.authentication_mixins import Authentication
from apps.posts.api.serializers.general_serializers import ExpeditionSerializer, BirdSerializer, SightingSerializer, ContributionSerializer

class ExpeditionViewSet(Authentication, viewsets.ModelViewSet): #En ExpeditionsViewSet se ve cómo se sobre escriben los métodos para personalizarlos
    serializer_class = ExpeditionSerializer

    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(state=True)
        return queryset
       
    def create(self, request):
        '''
        Crea una expedición

        '''
        serializer = self.serializer_class(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        # do your customization here
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request):
        '''
        Lista todas las expediciones

        '''
        expedition_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(expedition_serializer.data, status = status.HTTP_200_OK)

    def update(self, request, pk=None):
        '''
        Actualiza una expedición

        '''
        expedition = self.get_queryset().filter(id = pk).first()
        if expedition:
            expedition_serializer = self.serializer_class(expedition, data = request.data)
            if expedition_serializer.is_valid():
                expedition_serializer.save()
                return Response(expedition_serializer.data, status = status.HTTP_200_OK)
            return Response(expedition_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        '''
        Elimina una expedición

        '''
        expedition = self.get_queryset().filter(id = pk).first()
        if expedition:
            expedition.state = False
            expedition.save()
            return Response({'message': 'Expedición eliminada correctamente' }, status = status.HTTP_200_OK)
        return Response({'message': 'No existe esa expedición' }, status = status.HTTP_400_BAD_REQUEST)


class ContributionViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ContributionSerializer
    
    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(state=True)
        return queryset


'''class ExpeditionListAPIView(generics.ListAPIView):
    serializer_class = ExpeditionSerializer
    
    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(state=True)
        return queryset

    def post(self, request): #Sobre escrbiendo el método
        serializer = self.serializer_class(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"mesage": "Expedición creada correctamente"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ExpeditionCreatedAPIView(generics.CreateAPIView):
    serializer_class = ExpeditionSerializer

class ExpeditionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ExpeditionSerializer

    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(state=True)
        return queryset

class ExpeditionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ExpeditionSerializer

    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(state=True)
        return queryset
    
    def delete(self, request, pk=None):
        expedition = self.get_queryset().filter(id = pk).first()
        if expedition:
            expedition.state = False
            expedition.save()
            return Response({'message': 'Expedición eliminada correctamente' }, status = status.HTTP_200_OK)
        return Response({'message': 'No existe esa expedición' }, status = status.HTTP_400_BAD_REQUEST)

class ExpeditionUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ExpeditionSerializer

    def get_queryset(self, pk):
    
        queryset = self.serializer_class.Meta.model.objects.filter(state=True).filter(id = pk).first()
        return queryset

    def patch(self, request, pk=None):
        expedition = self.get_queryset(pk)
        if expedition:
            expedition_serializer = self.serializer_class(expedition)
            return Response(expedition_serializer.data, status = status.HTTP_200_OK)
        return Response({'message': 'No existe esa expedición' }, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        expedition = self.get_queryset(pk)
        if expedition:
            expedition_serializer = self.serializer_class(expedition, data = request.data)
            if expedition_serializer.is_valid():
                expedition_serializer.save()
                return Response(expedition_serializer.data, status = status.HTTP_200_OK)
            return Response(expedition_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
'''

