from apps.users.models import User, Achievement
from datetime import datetime

FIRST_EXPEDITION = 'Primera expedición'
FIRST_CONTRIBUTION = 'Primera contribución'


class AchievementsCheckers(object):

    def create_user_achievement(self, user, achievement_name):
        achievement = Achievement.objects.filter(name=achievement_name).first()
        print(achievement)
        user.achievements.add(achievement, through_defaults={'unlock_date': datetime.now()})
        return achievement_name

    def check_first_expedition(self, user):  # Logro de primera publicación
        # print(user.achievements.all())
        if user.achievements is None:
            print('entré 1')
            return self.create_user_achievement(user, FIRST_EXPEDITION)

        achievement = user.achievements.filter(name=FIRST_EXPEDITION)
        print(achievement)
        if not achievement:
            print('entré 2')
            return self.create_user_achievement(user, FIRST_EXPEDITION)

        print('entré 3')
        return None

    def check_first_contribution(self, user):  # Logro de primera contribución
        achievement = user.achievements.objects.filter(name=FIRST_CONTRIBUTION)
        if achievement is None:
            self.create_user_achievement(user, FIRST_CONTRIBUTION)
            return FIRST_CONTRIBUTION
        return None
