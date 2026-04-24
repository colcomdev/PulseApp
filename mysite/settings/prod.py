from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Static files (important for AWS)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'