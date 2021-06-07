from apps.users.authentication_mixins import Authentication
from apps.users.models import User


LEVEL_NAME = [
    'Colibrí', 'Jacamará coliverde', 'Tángara azulada', 'Pájaro péndulo', 'Cacique candela', 'Perico cara sucia',
    'Jacana común', 'Tucán pechiblanco', 'Aruco', 'Murruco', 'Corocoro rojo'
]

CONTRIBUTION_CONFIRMATION_XP_VALUE = 25



class UserXpUtils:

    def check_level(self, user):
        current_xp_level = user.xp
        level_name_before_check = user.level_name

        if 0 <= current_xp_level < 500:
            user.level_name = LEVEL_NAME[0]

        elif 500 <= current_xp_level < 1000:
            user.level_name = LEVEL_NAME[1]

        elif 1000 <= current_xp_level < 2000:
            user.level_name = LEVEL_NAME[2]

        elif 2000 <= current_xp_level < 3000:
            user.level_name = LEVEL_NAME[3]

        elif 3000 <= current_xp_level < 4000:
            user.level_name = LEVEL_NAME[4]

        elif 4000 <= current_xp_level < 5000:
            user.level_name = LEVEL_NAME[5]

        elif 5000 <= current_xp_level < 6000:
            user.level_name = LEVEL_NAME[6]

        elif 6000 <= current_xp_level < 7000:
            user.level_name = LEVEL_NAME[7]

        elif 7000 <= current_xp_level < 8000:
            user.level_name = LEVEL_NAME[8]

        elif 8000 <= current_xp_level < 9000:
            user.level_name = LEVEL_NAME[9]

        elif current_xp_level >= 9000:
            user.level_name = LEVEL_NAME[10]

        if level_name_before_check == user.level_name:
            return None
        user.save()
        return user.level_name

    def add_xp(self, user, value):
        user.xp += value
        user.save()

    def check_user_contributions(self, sighting):
        for c in sighting.contribution_set.iterator():
            if c.vote == sighting.is_correct:
                self.add_xp(c.user, CONTRIBUTION_CONFIRMATION_XP_VALUE)




