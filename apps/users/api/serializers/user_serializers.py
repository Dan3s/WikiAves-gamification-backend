import datetime
from abc import ABC

from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed

from apps.posts.models import Sighting
from apps.users.models import User


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'last_names')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])  # Para encriptar la contraseña
        user.save()
        return user

    def update(self, instance, validate_data):
        update_user = super().update(instance, validate_data)  # Para que haga su atualización automatica
        update_user.set_password(validate_data['password'])  # Para que se encripte la contraseña cuando se guarde
        update_user.save()
        return update_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'name': instance['name'],
            'last_names': instance['last_names'],
            'username': instance['username'],
            'password': instance['password'],
            'email': instance['email'],
            'city': instance['city'],
            'region': instance['region'],
            'experience': instance['xp'],
            'level': instance['level_name']
        }


class UserRankingSerializer(serializers.ModelSerializer):
    # achievements = serializers.SerializerMethodField('get_achievements_count')

    def get_achievements_count(self, obj):
        return obj.achievements.count()

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'city': instance.city,
            'region': instance.region,
            'experience': instance.xp,
            'level': instance.level_name,
            'achievements': self.get_achievements_count(instance)
        }


class UserProfileStatisticsSerializer(serializers.ModelSerializer):

    def get_quantity_species(self, user):
        query_expeditions = user.expedition_set.all()
        sightings_list = Sighting.objects.none()

        for e in query_expeditions.iterator():
            sightings_list |= e.sighted_birds.all().distinct()

        return sightings_list.count()

    def get_quantity_photos(self, user):
        query_expeditions = user.expedition_set
        photos_count = 0

        for e in query_expeditions.iterator():
            for s in e.sighting_set.iterator():
                photos_count += s.sighting_photos.count()
        return photos_count

    def get_achievements_count(self, obj):
        return obj.achievements.count()

    def get_expeditions_count(self, obj):
        return obj.expedition_set.count()

    def get_last_login(self, obj):
        # print(obj.historical.most_recent().last_login = datetime.datetime.now())
        # print(User.historical.get_history_user(obj).all().filter(username=obj.username).last())
        # print(obj.historical.last().fi)
        return obj.historical.most_recent().last_login

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'last_names': instance.last_names,
            'username': instance.username,
            # 'password': instance.password,
            'email': instance.email,
            'city': instance.city,
            'region': instance.region,
            'experience': instance.xp,
            'level': instance.level_name,
            'achievements': self.get_achievements_count(instance),
            'expeditions': self.get_expeditions_count(instance),
            'photos': self.get_quantity_photos(instance),
            'species': self.get_quantity_species(instance),
            'pages_visited': instance.pages_visited,
            'last_login': instance.last_login

        }


class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email', '')
        return super().validate(attrs)

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=64, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields=['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('El link de reestablecimiento de contraseña es inválido', 401)
            user.set_password(password)
            user.save()
            return user
        except Exception as e:
            raise AuthenticationFailed('El link de reestablecimiento de contraseña es inválido', 401)
        return super().validate(attrs)

