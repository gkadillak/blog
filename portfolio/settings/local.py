from .base import *
import os
DEBUG = True


os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings.local'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
    }
}
