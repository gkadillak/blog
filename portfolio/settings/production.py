from .base import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'blog_database_user',
        'PASSWORD': environ('DATABASE_PASSWORD'),
        'PORT': '',
    }
}
