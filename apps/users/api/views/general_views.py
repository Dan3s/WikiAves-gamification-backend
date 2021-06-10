from django.http import HttpResponsePermanentRedirect
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.generics import RetrieveAPIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from WikiAves_gamification_backend.settings.base import FRONTEND_URL
from apps.users.models import Achievement
from apps.users.api.serializers.achievement_serializers import AchievementSerializer, UserAchievementSerializer
from apps.users.api.serializers.user_serializers import UserRankingSerializer, \
    UserProfileStatisticsSerializer, ResetPasswordEmailSerializer, SetNewPasswordSerializer
from apps.users.authentication_mixins import Authentication
from apps.posts.utils.email_utils import EmailUtils
from apps.users.models import User


class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = ['http', 'https']


class AchievementListAPIView(Authentication, generics.ListAPIView):
    serializer_class = AchievementSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        queryset = Achievement.objects.all()
        return queryset


class ProfileView(Authentication, generics.RetrieveAPIView):
    serializer_class = UserProfileStatisticsSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        queryset = self.serializer_class.Meta.model.objects.filter(id=user_id)

        obj = queryset.get()
        return queryset


class UsersStatistics(Authentication, ReadOnlyModelViewSet):
    serializer_class = UserProfileStatisticsSerializer

    def get_queryset(self):
        # user_id = self.kwargs['id']
        # queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.filter(is_active=True)
        if (self.user.is_staff):
            return queryset
        else:
            return Response({'message': 'Permisos de usuario insuficientes'}, status=status.HTTP_401_UNAUTHORIZED)


class UserAchievementsListAPIView(Authentication, generics.ListAPIView):
    serializer_class = UserAchievementSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        user_id = self.kwargs['pk']
        queryset = self.serializer_class.Meta.model.objects.filter(user=user_id)
        return queryset


class UserRankingListAPIView(Authentication, generics.ListAPIView):
    serializer_class = UserRankingSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        queryset = self.serializer_class.Meta.model.objects.all().order_by('-xp')
        return queryset


class UserRankingByRegionListAPIView(Authentication, generics.ListAPIView):
    serializer_class = UserRankingSerializer

    def get_queryset(self):
        # queryset = super(CLASS_NAME, self).get_queryset()
        region = self.kwargs['region']
        queryset = self.serializer_class.Meta.model.objects.filter(region=region).order_by('-xp')
        return queryset


class RequestPasswordResetEmailGenericAPIView(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailSerializer

    def post(self, request):
        data = {'request': request, 'data': request.data}
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relative_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url=request.data.get('redirect_url', '')
            absurl = 'http://' + current_site + relative_link
            email_body = '¡Hola! \nUsa el siguiente link para reestablecer tu contraseña:\n' \
                         + absurl+'?redirect_url='+redirect_url
            email_data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reestablecer contraseña'}
            email_utils = EmailUtils()
            email_utils.send_recovery_password_email(email_data)
        return Response({'message': 'Se ha enviado un link para reestablecer tu contraseña'}, status=status.HTTP_200_OK)


class PasswordTokenCheckGenericAPIView(generics.GenericAPIView):

    def get(self, request, uidb64, token):
        redirect_url = request.GET.get('redirect_url')
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url+'?token_valid=False')
                else:
                    return CustomRedirect(FRONTEND_URL + '?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(redirect_url+'?token_valid=True&?message=Credenciales válidas&?uidb64='+uidb64+'&?token='+token)
            else:
                return CustomRedirect(FRONTEND_URL + '?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user, token):
                return CustomRedirect(redirect_url + '?token_valid=False')

class SetNewPasswordGenericAPIView(generics.GenericAPIView):
    serializer_class =  SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Contraseña reeestablecida correctamente'}, status=status.HTTP_200_OK)
