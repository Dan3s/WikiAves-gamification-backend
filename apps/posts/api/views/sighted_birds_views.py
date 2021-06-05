from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView

from apps.posts.api.serializers.general_serializers import SightingSerializer, BirdSerializer
from apps.posts.utils.sighting_utils import SightingUtils
from apps.users.authentication_mixins import Authentication


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
        expedition_id = self.kwargs['id']
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
                return Response(serializer.data, status = status.HTTP_200_OK)
            return Response({"message": "El ave ya existe", "bird_id": bird_id}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




