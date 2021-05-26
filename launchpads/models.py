
import space_django.api

from rockets.models import Rocket

from django.db import models

class Launchpad(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    sanitized_name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    launch_attempts = models.IntegerField()
    launch_successes = models.IntegerField()
    rockets = models.ManyToManyField(Rocket, null=True)
    details = models.TextField()
    status = models.CharField(max_length=100)
    id = models.CharField(max_length=24, primary_key=True)

    class Meta:
        verbose_name = 'Launchpad'
        verbose_name_plural = 'Launchpads'

    def __str__(self):
        return self.name

class LaunchpadImage(models.Model):
    launchpad = models.ForeignKey(Launchpad, on_delete=models.SET_NULL, null=True)
    image_location = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Launchpad Image'
        verbose_name_plural = 'Launchpad Images'
    
    def __str__(self):
        return str(self.id)
