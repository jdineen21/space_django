import datetime
import space_django.api
import logging

from operator import itemgetter

from launchpads.models import Launchpad
from rockets.models import Rocket

from django.db import models

class Launch(models.Model):
    fairings = models.JSONField(null=True)
    links = models.JSONField()
    static_fire_date_utc = models.DateTimeField(null=True)
    static_fire_date_unix = models.IntegerField(null=True)
    tbd = models.BooleanField()
    net = models.BooleanField()
    window = models.IntegerField(null=True)
    rocket = models.ForeignKey(Rocket, on_delete=models.SET_NULL, null=True)
    success = models.BooleanField(null=True)
    details = models.TextField(null=True)
    launchpad = models.ForeignKey(Launchpad, on_delete=models.SET_NULL, null=True)
    auto_update = models.BooleanField()
    launch_library_id = models.CharField(max_length=100, null=True)
    flight_number = models.IntegerField()
    name = models.CharField(max_length=100)
    date_utc = models.DateTimeField(null=True)
    date_unix = models.IntegerField(null=True)
    date_local = models.DateTimeField(null=True)
    date_precision = models.CharField(max_length=100, null=True)
    upcoming = models.BooleanField()
    id = models.CharField(max_length=24, primary_key=True)

    def __str__(self):
        return self.name

class Launches:

    def all():
        all_launches = space_django.api.external_cached('launches/', 86400)
        return sorted(all_launches, key=itemgetter('flight_number'), reverse=True)

    def next():
        return space_django.api.external_cached('launches/next/', 86400)

    def past():
        past_launches = space_django.api.external_cached('launches/past/', 86400)

        # # Add datetime value to each dictionary in list
        # for i in range(len(past_launches)):
        #     launch_datetime = datetime.datetime.fromtimestamp(past_launches[i]['date_unix'])
        #     past_launches[i]['launch_datetime'] = launch_datetime

        return past_launches[::-1]

    def upcoming():
        upcoming_launches = space_django.api.external_cached('launches/upcoming/', 86400)

        # # Add datetime value to each dictionary in list
        # for i in range(len(upcoming_launches)):
        #     launch_datetime = datetime.datetime.fromtimestamp(upcoming_launches[i]['date_unix'])
        #     upcoming_launches[i]['launch_datetime'] = launch_datetime

        return upcoming_launches

    def by_flight_number(flight_number):
        url_affix = 'launches/%s/' % flight_number
        launch_by_flight_number = space_django.api.external_cached(url_affix, 86400)
        
        # # Add datetime value to dictionary
        # launch_datetime = datetime.datetime.fromtimestamp(launch_by_flight_number['date_unix'])
        # launch_by_flight_number['launch_datetime'] = launch_datetime

        return launch_by_flight_number
    
    def by_id(id):
        url_affix = 'launches/%s/' % id
        launch_by_id = space_django.api.external_cached(url_affix, 86400)

        return launch_by_id

    # def get_related(id):
    #     all_launches = Launches.all()
    #     for launch in all_launches:
        