
from space_django import api

from .models import Launch
from launchpads.models import Launchpad
from rockets.models import Rocket

from django.utils import dateparse

def update():
    data = api.external('launches/')

    launchs = []
    for i, launch in enumerate(data):
        launch.pop('crew', None)
        launch.pop('ships', None)
        launch.pop('capsules', None)
        launch.pop('payloads', None)
        launch.pop('failures', None)
        launch.pop('cores', None)
        launch['rocket'] = Rocket.objects.get(id=launch['rocket'])
        launch['launchpad'] = Launchpad.objects.get(id=launch['launchpad'])
        launchs.append(Launch(**launch))

    Launch.objects.all().delete()
    Launch.objects.bulk_create(launchs)
