from .base import *
import dj_database_url
from decouple import config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['wiki-aves-backend.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'du4fku0n449pf',
        'USER': 'sizigvztpkducd',
        'PASSWORD': '013825dfa80ff4666d505adc26c1b704e10619bc0062ff29b9e8dd978e53e6d7',
        'HOST': 'ec2-23-22-191-232.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

'''DATABASE ={
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}'''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
  #  os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorafe'