
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Security

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 63072000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'spacextrack',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'read_default_file': '/var/www/spacextrack.com/my.cnf',
            'init_command': 'SET default_storage_engine=INNODB',
        },
    }
}

# Caching
# https://docs.djangoproject.com/en/3.1/ref/settings/#caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}