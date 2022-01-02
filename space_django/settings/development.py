
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Caching
# https://docs.djangoproject.com/en/4.0/ref/settings/#caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Logging
# https://docs.djangoproject.com/en/4.0/ref/settings/#logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}