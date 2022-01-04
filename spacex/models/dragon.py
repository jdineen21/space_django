from django.db import models

from .image import Image

class Dragon(models.Model):
    IMAGE_PATHS = [
        ('image', 'flickr_images'),
    ]
    images = models.ManyToManyField(Image)
    heat_shield = models.JSONField()
    launch_payload_mass = models.JSONField()
    launch_payload_vol = models.JSONField()
    return_payload_mass = models.JSONField()
    return_payload_vol = models.JSONField()
    pressurized_capsule = models.JSONField()
    trunk = models.JSONField()
    height_w_trunk = models.JSONField()
    diameter = models.JSONField()
    first_flight = models.DateField()
    flickr_images = models.JSONField()
    name = models.CharField(max_length=100)
    sanitized_name = models.CharField(max_length=100)
    active = models.BooleanField()
    crew_capacity = models.IntegerField()
    sidewall_angle_deg = models.IntegerField()
    orbit_duration_yr = models.IntegerField()
    dry_mass_kg = models.IntegerField()
    dry_mass_lb = models.IntegerField()
    thrusters = models.JSONField()
    wikipedia = models.CharField(max_length=100)
    description = models.TextField()
    id = models.CharField(max_length=24, primary_key=True)

    class Meta:
        verbose_name = 'Dragon'
        verbose_name_plural = 'Dragons'

    def __str__(self):
        return self.name
