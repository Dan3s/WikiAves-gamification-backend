from apps.posts.utils.achievement_utils import AchievementsCheckers
from apps.posts.utils.email_utils import EmailUtils
from apps.posts.utils.user_xp_utils import ADD_SIGHTING_XP_VALUE, UserXpUtils, CONTRIBUTION_XP_VALUE
from apps.users.models import User
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

    def create(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            serializer.save()
            achievements_utils = AchievementsCheckers()
            xp_utils = UserXpUtils()

            achievement_name, achievement_descript = achievements_utils.check_first_sighting(self.user)
            if achievement_name is None:
                xp_utils.add_xp(self.user, ADD_SIGHTING_XP_VALUE)

            level_unlocked = xp_utils.check_level(self.user)
            achievement_level_name, achievement_level_descript = achievements_utils.check_levels_achievement(
                self.user)
            return Response({"message": "Avistamiento creado correctamente", "achieve_name": achievement_name,
                             "achieve_description": achievement_descript,
                             "level_up": level_unlocked, "achieve_level_name": achievement_level_name,
                             "achieve_level_descript": achievement_level_descript}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):

        user = self.user
        user.pages_visited += 1
        user.save()
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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
        achievement_name, achievement_descript = '', ''
        level_unlocked = ''
        achievement_level_name, achievement_level_descript = '', ''


        sighting_id = self.kwargs['sighting_id']
        recipient_email = [Sighting.objects.filter(id=sighting_id).first().expedition.user.email]
        interaction_type = self.kwargs['type']

        if interaction_type == CONTRIBUTION_TYPE[0]:  # like
            sighting_utils = SightingUtils()
            sighting_utils.increase_like(sighting_id)
            email = EmailUtils()
            email.send_notification_email(recipient_email, self.user.username)
        elif interaction_type == CONTRIBUTION_TYPE[1]:  # vote
            sighting_utils = SightingUtils()
            achievements_utils = AchievementsCheckers()
            xp_utils = UserXpUtils()

            achievement_name, achievement_descript = achievements_utils.check_first_contribution(self.user)
            if achievement_name is None:
                xp_utils.add_xp(self.user, CONTRIBUTION_XP_VALUE)

            level_unlocked = xp_utils.check_level(self.user)
            achievement_level_name, achievement_level_descript = achievements_utils.check_levels_achievement(
                self.user)

            try:
                if request.data['vote'] or not request.data['vote']:
                    sighting_utils.create_user_vote_contribution(self.user, sighting_id, request.data['vote'])
                    email = EmailUtils()
                    email.send_notification_email(recipient_email, self.user.username, request.data['vote'])
            except:
                return Response({'message': 'El atributo del body vote debe ser true o false, booleano sin comillas'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Error en parámetro type'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Interacción realizada correctamente", "achieve_name": achievement_name,
                         "achieve_description": achievement_descript,
                         "level_up": level_unlocked, "achieve_level_name": achievement_level_name,
                         "achieve_level_descript": achievement_level_descript}, status=status.HTTP_200_OK)
