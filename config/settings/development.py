# flake8: noqa: F405

from .base import *


SECRET_KEY = 'i_am_a_super_secret_key'
DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
