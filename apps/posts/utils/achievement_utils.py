from apps.users.models import User, Achievement
from .user_xp_utils import UserXpUtils
from datetime import datetime

FIRST_EXPEDITION = 'Primera expedición'
FIRST_CONTRIBUTION = 'Primera contribución'


class AchievementsCheckers(object):

    def create_user_achievement(self, user, achievement_name):
        achievement = Achievement.objects.filter(name=achievement_name).first()
        user.achievements.add(achievement, through_defaults={'unlock_date': datetime.now()})
        UserXpUtils.add_xp(user, achievement.xp_value)
        return achievement_name

    def check_first_expedition(self, user):  # Logro de primera publicación
        # print(user.achievements.all())
        if user.achievements is None:
            return self.create_user_achievement(user, FIRST_EXPEDITION)

        achievement = user.achievements.filter(name=FIRST_EXPEDITION)

        if not achievement:
            return self.create_user_achievement(user, FIRST_EXPEDITION)

        return None

    def check_first_contribution(self, user):  # Logro de primera contribución. (Hacer vista)
        achievement = user.achievements.objects.filter(name=FIRST_CONTRIBUTION)
        if user.achievements is None:
            return self.create_user_achievement(user, FIRST_EXPEDITION)

        achievement = user.achievements.filter(name=FIRST_EXPEDITION)

        if not achievement:
            return self.create_user_achievement(user, FIRST_EXPEDITION)

        return None
