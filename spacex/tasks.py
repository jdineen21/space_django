
import logging

from space_django import api

from .models import Launchpad
from rockets.models import Rocket
from launches.models import Launch

def update():
    data = api.external('launchpads/')

    for i, launchpad_data in enumerate(data):
        launches = launchpad_data['launches']
        rockets = launchpad_data['rockets']

        launchpad_data.pop('launches', None)
        launchpad_data.pop('rockets', None)

        sanitized_name = launchpad_data['name'].replace(' ','_').lower()

        object, created = Launchpad.objects.update_or_create(sanitized_name=sanitized_name, **launchpad_data)

        print(('[CREATED] %s') % object.name if created else ('[UPDATED] %s') % object.name)

        for rocket in rockets:
            object.rockets.set(rocket)

def purge():
    Launchpad.objects.all().delete()
