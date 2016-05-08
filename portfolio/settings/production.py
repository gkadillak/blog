from .base import *
import os

DEBUG = False


environ('DJANGO_SETTINGS_MODULE') = 'portfolio.settings.production'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'blog_database_user',
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'PORT': '',
    }
}
