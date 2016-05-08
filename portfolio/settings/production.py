from .base import *
import os

DEBUG = False


os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings.production'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'blog_database_user',
        'HOST': 'localhost',
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'PORT': '',
    }
}
