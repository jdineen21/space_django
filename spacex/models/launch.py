
from django.db import models

from .rocket import Rocket
from .launchpad import Launchpad

class Launch(models.Model):
    significant = models.BooleanField(default=False)
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

    class Meta:
        verbose_name_plural = "launches"

    def __str__(self):
        return self.name
