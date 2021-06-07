from rest_framework import serializers
from itertools import chain

from apps.posts.models import Sighting
from apps.posts.utils.user_xp_utils import UserXpUtils
from apps.users.authentication_mixins import Authentication
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


class UserProfileSerializer(serializers.ModelSerializer):

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
            'pages_visited': instance.pages_visited

        }
