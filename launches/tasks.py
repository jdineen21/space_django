
from space_django import api

from .models import Launch
from launchpads.models import Launchpad
from rockets.models import Rocket

from django.utils import dateparse

def update():
    data = api.external('launches/')

    launchs = []
    for i, launch in enumerate(data):
        if launch['static_fire_date_utc'] is not None:
            launch['static_fire_datetime'] = dateparse.parse_datetime(launch['static_fire_date_utc'])
        launch['datetime_utc'] = dateparse.parse_datetime(launch['date_utc'])
        launch['datetime_local'] = dateparse.parse_datetime(launch['date_local'])
        launch['datetime_precision'] = dateparse.parse_datetime(launch['date_precision'])
        launch.pop('static_fire_date_utc', None)
        launch.pop('static_fire_date_unix', None)
        #launch.pop('rocket', None)
        launch.pop('crew', None)
        launch.pop('ships', None)
        launch.pop('capsules', None)
        launch.pop('payloads', None)
        launch.pop('failures', None)
        launch.pop('date_utc', None)
        launch.pop('date_unix', None)
        launch.pop('date_local', None)
        launch.pop('date_local', None)
        launch.pop('date_precision', None)
        launch.pop('cores', None)
        launch['rocket'] = Rocket.objects.get(id=launch['rocket'])
        launch['launchpad'] = Launchpad.objects.get(id=launch['launchpad'])
        launchs.append(Launch(**launch))

    Launch.objects.all().delete()
    Launch.objects.bulk_create(launchs)
