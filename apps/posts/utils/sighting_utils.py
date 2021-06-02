from apps.posts.models import Bird


class SightingUtils(object):

    def bird_already_exists(self, scientific_name):
        bird = Bird.objects.filter(scientific_name=scientific_name).first()

        if not bird:
            return None
        bird.sightings += 1
        bird.save()

        return bird.id
