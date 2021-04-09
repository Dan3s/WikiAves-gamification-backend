from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

#from apps.posts.models import Expedition, Bird, Sighting
from apps.posts.api.serializers.general_serializers import ExpeditionSerializer, BirdSerializer, SightingSerializer, ContributionSerializer

class ExpeditionListAPIView(generics.ListAPIView):
    serializer_class = ExpeditionSerializer
    
    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.all()
        return queryset

    def post(self, request): #Sobre escrbiendo el método
        serializer = self.serializer_class(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({"mesage": "Expedición creada correctamente"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ExpeditionCreatedAPIView(generics.CreateAPIView):
    serializer_class = ExpeditionSerializer

class ContributionListAPIView(generics.ListAPIView):
    serializer_class = ContributionSerializer
    
    def get_queryset(self):
        #queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.all()
        return queryset