from django.db import models

from .image import Image

class Crew(models.Model):
    IMAGE_PATHS = [
        ('portrait', 'image'),
    ]
    images = models.ManyToManyField(Image)
    name = models.CharField(max_length=100)
    sanitized_name = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    wikipedia = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    id = models.CharField(max_length=24, primary_key=True)

    class Meta:
        verbose_name = 'Crew'
        verbose_name_plural = 'Crew'

    def __str__(self):
        return self.name
