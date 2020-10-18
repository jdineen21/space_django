
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

# Caching
# https://docs.djangoproject.com/en/3.1/ref/settings/#caching

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}