from apps.users.models import User, Achievement
from .user_xp_utils import UserXpUtils, LEVEL_NAME
from datetime import datetime

FIRST_SIGHTING = 'Primer avistamiento'
FIRST_CONTRIBUTION = 'Primera contribución'
FIRST_CORRECT_CONTRIBUTION = 'Primera contribución correcta'
LEVEL_THREE = 'Nivel Pájaro Péndulo alcanzado'
LEVEL_SEVEN = 'Nivel Tucán Pechiblanco alcanzado'
LEVEL_TEN = 'Nivel Corocoro Rojo alcanzado'


class AchievementsCheckers(object):

    def create_user_achievement(self, user, achievement_name):
        achievement = Achievement.objects.filter(name=achievement_name).first()
        user.achievements.add(achievement, through_defaults={'unlock_date': datetime.now()})
        user_xp = UserXpUtils()
        user_xp.add_xp(user, achievement.xp_value)
        return achievement.name, achievement.description

    def check_first_sighting(self, user):  # Logro de primer avistamiento
        if user.achievements is None:
            return self.create_user_achievement(user, FIRST_SIGHTING)

        achievement = user.achievements.filter(name=FIRST_SIGHTING)

        if not achievement:
            return self.create_user_achievement(user, FIRST_SIGHTING)

        return None, None

    def check_first_contribution(self, user):  # Logro de primera contribución.
        if user.achievements is None:
            return self.create_user_achievement(user, FIRST_CONTRIBUTION)

        achievement = user.achievements.filter(name=FIRST_CONTRIBUTION)

        if not achievement:
            return self.create_user_achievement(user, FIRST_CONTRIBUTION)

        return None, None

    def check_levels_achievement(self, user):
        achieve_level_three = user.achievements.filter(name=LEVEL_THREE)
        achieve_level_seven = user.achievements.filter(name=LEVEL_SEVEN)
        achieve_level_ten = user.achievements.filter(name=LEVEL_TEN)

        if not achieve_level_three and user.level_name == LEVEL_NAME[3]:
            return self.create_user_achievement(user, LEVEL_THREE)

        if not achieve_level_seven and user.level_name == LEVEL_NAME[7]:
            return self.create_user_achievement(user, LEVEL_SEVEN)

        if not achieve_level_ten and user.level_name == LEVEL_NAME[10]:
            return self.create_user_achievement(user, LEVEL_TEN)

        return None, None

    def check_first_contribution_correct(self, user):  # Logro de primera contribución correcta.
        achievement = user.achievements.filter(name=FIRST_CORRECT_CONTRIBUTION)

        if not achievement:
            return self.create_user_achievement(user, FIRST_CORRECT_CONTRIBUTION)

        return None, None

