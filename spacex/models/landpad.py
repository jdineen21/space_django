from django.db import models

from .image import Image

class Landpad(models.Model):
    IMAGE_PATHS = [
        ('image', 'images.large'),
    ]
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    sanitized_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    landing_attempts = models.IntegerField()
    landing_successes = models.IntegerField()
    wikipedia = models.CharField(max_length=100)
    details = models.TextField()
    status = models.CharField(max_length=100)
    id = models.CharField(max_length=24, primary_key=True)

    class Meta:
        verbose_name = 'Landpad'
        verbose_name_plural = 'Landpads'

    def __str__(self):
        return self.name
