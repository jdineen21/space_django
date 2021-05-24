
from space_django import api

from .models import Rocket

from django.utils import dateparse

def update():
    data = api.external('rockets/')

    rockets = []
    for i, rocket in enumerate(data):
        rockets.append(Rocket(**rocket))

    Rocket.objects.all().delete()
    Rocket.objects.bulk_create(rockets)
