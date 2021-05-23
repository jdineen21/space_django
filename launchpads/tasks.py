
from space_django import api
from .models import Launchpad

def update():
    data = api.external('launchpads/')

    Launchpads = []
    for i, launchpad in enumerate(data):
        launchpad.pop('rockets', None)
        launchpad.pop('launches', None)
        Launchpads.append(Launchpad(sanitized_name=launchpad['name'].replace(' ','_').lower(), **launchpad))

    Launchpad.objects.all().delete()
    Launchpad.objects.bulk_create(Launchpads)    
