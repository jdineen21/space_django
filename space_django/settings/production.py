
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['www.spacextrack.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database/db.sqlite3'),
    }
}