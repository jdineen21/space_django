
from django.utils.text import slugify

from space_django import api
from spacex.models import Launch, Launchpad, Rocket

class Database:

    def update():
        launches_data = api.external('launches/')
        launchpads_data = api.external('launchpads/')
        rockets_data = api.external('rockets/')

        print('-- ROCKETS --')
        for rocket_data in rockets_data:
            sanitized_name = slugify(rocket_data['name'])

            object, created = Rocket.objects.update_or_create(sanitized_name=sanitized_name, **rocket_data)

            print(('[CREATED] %s') % object.name if created else ('[UPDATED] %s') % object.name)

        print('-- LAUNCHPADS --')
        for launchpad_data in launchpads_data:
            rockets = launchpad_data['rockets']

            launchpad_data.pop('launches', None)
            launchpad_data.pop('rockets', None)

            sanitized_name = slugify(launchpad_data['name'])

            object, created = Launchpad.objects.update_or_create(sanitized_name=sanitized_name, **launchpad_data)

            print(('[CREATED] %s') % object.name if created else ('[UPDATED] %s') % object.name)

            for rocket in rockets:
                object.rockets.add(rocket)

        print('-- LAUNCHES --')
        for launch_data in launches_data:
            # rockets = launches_data['rockets']
            # launchpads = launches_data['launchpad']

            launch_data.pop('crew', None)
            launch_data.pop('ships', None)
            launch_data.pop('capsules', None)
            launch_data.pop('payloads', None)
            launch_data.pop('failures', None)
            launch_data.pop('cores', None)
            launch_data.pop('launches', None)
            launch_data.pop('rockets', None)
            launch_data['rocket'] = Rocket.objects.get(id=launch_data['rocket'])
            launch_data['launchpad'] = Launchpad.objects.get(id=launch_data['launchpad'])

            object, created = Launch.objects.update_or_create(**launch_data)

            print(('[CREATED] %s') % object.name if created else ('[UPDATED] %s') % object.name)

            # for rocket in rockets:
            #     object.rockets.add(rocket)

    def purge():
        Launch.objects.all().delete()
        Launchpad.objects.all().delete()
        Rocket.objects.all().delete()
