from rest_framework import serializers

from apps.users.models import Achievement, UserAchievement, User


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'

    '''def to_representation(self, instance):
        return {
            'name': instance.name,
            'description': instance.description,
            #'icon': instance.icon,
            'xp_value': instance.xp_value
            #'unlock_date': instance.userachievement_set.all().filter(achievement= instance.id).first().unlock_date
        }'''


class UserAchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAchievement
        exclude = ('id', 'user',)

    def to_representation(self, instance):
        return {
            'name': instance.achievement.name,
            'description': instance.achievement.description,
            'xp_value': instance.achievement.xp_value,
            'unlock_date': instance.unlock_date
        }
