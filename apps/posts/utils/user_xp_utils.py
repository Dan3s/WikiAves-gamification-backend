# from apps.posts.utils.achievement_utils import AchievementsCheckers
from apps.posts.utils.email_utils import EmailUtils

LEVEL_NAME = [
    'Colibrí', 'Jacamará coliverde', 'Tángara azulada', 'Pájaro péndulo', 'Cacique candela', 'Perico cara sucia',
    'Jacana común', 'Tucán pechiblanco', 'Aruco', 'Murruco', 'Corocoro rojo'
]

CONTRIBUTION_CONFIRMATION_XP_VALUE = 25
CONTRIBUTION_XP_VALUE = 5
ADD_SIGHTING_XP_VALUE = 20


class UserXpUtils:

    def check_level(self, user):
        current_xp_level = user.xp
        level_name_before_check = user.level_name

        if 20 <= current_xp_level < 50:
            user.level_name = LEVEL_NAME[1]

        elif 50 <= current_xp_level < 80:
            user.level_name = LEVEL_NAME[2]

        elif 80 <= current_xp_level < 110:
            user.level_name = LEVEL_NAME[3]

        elif 110 <= current_xp_level < 140:
            user.level_name = LEVEL_NAME[4]

        elif 140 <= current_xp_level < 170:
            user.level_name = LEVEL_NAME[5]

        elif 170 <= current_xp_level < 200:
            user.level_name = LEVEL_NAME[6]

        elif 200 <= current_xp_level < 230:
            user.level_name = LEVEL_NAME[7]

        elif 230 <= current_xp_level < 260:
            user.level_name = LEVEL_NAME[8]

        elif 260 <= current_xp_level < 290:
            user.level_name = LEVEL_NAME[9]

        elif current_xp_level >= 300:
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
                email_data = {'email_body': '¡Hola! Queremos informarte que tu voto en el avistamiento del ave '
                                            + sighting.bird.scientific_name + ' ha sido correcto', 'to_email':
                                  c.user.email, 'email_subject': 'Contribución correcta'}
                email_utils = EmailUtils()
                email_utils.send_email(email_data)
            # AchievementsCheckers.check_first_contribution_correct(c.user)
