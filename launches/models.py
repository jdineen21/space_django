import datetime
import space_django.api

from django.db import models

class Launches:

    def all():
        all_launches = space_django.api.external_cached('launches/', 86400)

        # Add datetime value to each dictionary in list
        for i in range(len(all_launches)):
            launch_datetime = datetime.datetime.fromtimestamp(all_launches[i]['launch_date_unix'])
            all_launches[i]['launch_datetime'] = launch_datetime

        return all_launches[::-1]

    def next():
        return space_django.api.external_cached('launches/next/', 86400)

    def past():
        past_launches = space_django.api.external_cached('launches/past/', 86400)

        # Add datetime value to each dictionary in list
        for i in range(len(past_launches)):
            launch_datetime = datetime.datetime.fromtimestamp(past_launches[i]['launch_date_unix'])
            past_launches[i]['launch_datetime'] = launch_datetime

        return past_launches[::-1]

    def upcoming():
        upcoming_launches = space_django.api.external_cached('launches/upcoming/', 86400)

        # Add datetime value to each dictionary in list
        for i in range(len(upcoming_launches)):
            launch_datetime = datetime.datetime.fromtimestamp(upcoming_launches[i]['launch_date_unix'])
            upcoming_launches[i]['launch_datetime'] = launch_datetime

        return upcoming_launches

    def by_flight_number(flight_number):
        url_affix = 'launches/%s/' % flight_number
        launch_by_flight_number = space_django.api.external_cached(url_affix, 86400)
        
        # Add datetime value to dictionary
        launch_datetime = datetime.datetime.fromtimestamp(launch_by_flight_number['launch_date_unix'])
        launch_by_flight_number['launch_datetime'] = launch_datetime

        return launch_by_flight_number