from apps.posts.models import Bird, Sighting, Contribution
from apps.posts.utils.user_xp_utils import UserXpUtils


class SightingUtils(object):

    def bird_already_exists(self, scientific_name):
        bird = Bird.objects.filter(scientific_name=scientific_name).first()

        if not bird:
            return None
        bird.sightings += 1
        bird.save()

        return bird.id

    def increase_like(self, sighting_id):
        sighting = Sighting.objects.filter(id=sighting_id).first()
        sighting.likes += 1
        sighting.save()

    def create_user_vote_contribution(self, user, sighting_id, vote):
        contribution = Contribution(user=user, vote=vote)
        contribution.save()
        contribution.sightings.add(Sighting.objects.filter(id=sighting_id).first())
        contribution.save()

    def sighting_verification(self, sighting_id, is_correct):
        sighting = Sighting.objects.filter(id=sighting_id)
        sighting.is_verified = True
        sighting.is_correct = is_correct
        check_contributions = UserXpUtils()
        check_contributions.check_user_contributions(sighting)
        sighting.save()

