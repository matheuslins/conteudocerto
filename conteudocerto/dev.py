#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Django settings for dev. """

from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Templates

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    BASE_DIR,
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    BASE_DIR,
)

STATIC_URL = '/core/static/'

MEDIA_URL = '/media/'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']
