from rest_framework import serializers
from itertools import chain

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

    def create (self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])#Para encriptar la contraseña
        user.save()
        return user

    def update (self, instance, validate_data):
        update_user = super().update(instance, validate_data) #Para que haga su atualización automatica
        update_user.set_password(validate_data['password']) #Para que se encripte la contraseña cuando se guarde
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
    #achievements = serializers.SerializerMethodField('get_achievements_count')

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

    photos = None
    species = None


    def get_achievements_count(self, obj):
        return obj.achievements.count()

    def get_expeditions_count(self, obj):
        return obj.expedition_set.count()

    def set_photos_and_species(self, obj):
        query_expeditions = obj.expedition_set.all()
        #query_sightings = Sighting.object.all()
        #result_list = list(chain(query_expeditions, query_sightings))
        print('holaaaaaaa')

        for e in query_expeditions.iterator():
            print(e.name)
            for s in e.sighted_birds:
                self.photos += s.photo_set.count()
                self.species += s.bird_set.count()


    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        self.set_photos_and_species(instance)
        return {
            'id': instance.id,
            'name': instance.name,
            'last_names': instance.last_names,
            'username': instance.username,
            #'password': instance.password,
            'email': instance.email,
            'city': instance.city,
            'region': instance.region,
            'experience': instance.xp,
            'level': instance.level_name,
            'achievements': self.get_achievements_count(instance),
            'expeditions': self.get_expeditions_count(instance),
            'photos': self.photos,
            'species': self.species

        }
