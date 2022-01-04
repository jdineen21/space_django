from django.db import models
from django.core.paginator import Paginator

from .crew import Crew
from .image import Image
from .launchpad import Launchpad
from .rocket import Rocket

class Launch(models.Model):
    IMAGE_PATHS = [
        ('patch', 'links.patch.large'),
        ('image', 'links.flickr.original'),
    ]
    images = models.ManyToManyField(Image)
    significant = models.BooleanField(default=False)
    fairings = models.JSONField(
        blank=True,
        null=True,
    )
    links = models.JSONField()
    static_fire_date_utc = models.DateTimeField(
        blank=True, 
        null=True,
    )
    static_fire_date_unix = models.IntegerField(
        blank=True,
        null=True,
    )
    tbd = models.BooleanField()
    net = models.BooleanField()
    window = models.IntegerField(blank=True, null=True)
    rocket = models.ForeignKey(Rocket, on_delete=models.SET_NULL, null=True)
    success = models.BooleanField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    crew = models.ManyToManyField(Crew)
    launchpad = models.ForeignKey(Launchpad, on_delete=models.SET_NULL, null=True)
    auto_update = models.BooleanField()
    launch_library_id = models.CharField(max_length=100, blank=True, null=True)
    flight_number = models.IntegerField()
    name = models.CharField(max_length=100)
    sanitized_name = models.CharField(max_length=100)
    date_utc = models.DateTimeField(blank=True, null=True)
    date_unix = models.IntegerField(blank=True, null=True)
    date_local = models.DateTimeField(blank=True, null=True)
    date_precision = models.CharField(max_length=100, blank=True, null=True)
    upcoming = models.BooleanField()
    id = models.CharField(max_length=24, primary_key=True)

    class Meta:
        verbose_name = 'launch'
        verbose_name_plural = 'launches'
        ordering = ['flight_number']

    def __str__(self):
        return self.name
    
    def get_paginator(self):
        return Paginator(Launch.objects.all(), 1)
    