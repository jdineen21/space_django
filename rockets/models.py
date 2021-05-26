
from django.db import models

class Rocket(models.Model):
    height = models.JSONField()
    diameter = models.JSONField()
    mass = models.JSONField()
    first_stage = models.JSONField()
    second_stage = models.JSONField()
    engines = models.JSONField()
    landing_legs = models.JSONField()
    payload_weights = models.JSONField()
    flickr_images = models.JSONField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    active = models.BooleanField()
    stages = models.IntegerField()
    boosters = models.IntegerField()
    cost_per_launch = models.IntegerField()
    success_rate_pct = models.IntegerField()
    first_flight = models.DateField()
    country = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    wikipedia = models.CharField(max_length=100)
    description = models.TextField()
    id = models.CharField(max_length=24, primary_key=True)

    def __str__(self):
        return self.name
