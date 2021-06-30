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
    significant = models.BooleanField(default=False)
    fairings = models.JSONField(null=True)
    links = models.JSONField()
    images = models.ManyToManyField(Image)
    static_fire_date_utc = models.DateTimeField(null=True)
    static_fire_date_unix = models.IntegerField(null=True)
    tbd = models.BooleanField()
    net = models.BooleanField()
    window = models.IntegerField(null=True)
    rocket = models.ForeignKey(Rocket, on_delete=models.SET_NULL, null=True)
    success = models.BooleanField(null=True)
    details = models.TextField(null=True)
    crew = models.ManyToManyField(Crew)
    launchpad = models.ForeignKey(Launchpad, on_delete=models.SET_NULL, null=True)
    auto_update = models.BooleanField()
    launch_library_id = models.CharField(max_length=100, null=True)
    flight_number = models.IntegerField()
    name = models.CharField(max_length=100)
    sanitized_name = models.CharField(max_length=100)
    date_utc = models.DateTimeField(null=True)
    date_unix = models.IntegerField(null=True)
    date_local = models.DateTimeField(null=True)
    date_precision = models.CharField(max_length=100, null=True)
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
    
    def get_images(id, type):
        images = []
        for o in Launch.objects.get(id=id).images.filter(type=type):
            images.append(o.image.url)
        if len(images) == 1:
            images = images[0]
        return images
    