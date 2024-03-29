from spacex.models.launch import Launch
from django.db import models

from .launch import Launch

class Payload(models.Model):
    dragon = models.JSONField()
    name = models.CharField(max_length=100)
    sanitized_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    reused = models.BooleanField()
    launch = models.ForeignKey(Launch, on_delete=models.SET_NULL, null=True)
    customers = models.JSONField()
    norad_ids = models.JSONField(blank=True, null=True)
    nationalities = models.JSONField()
    manufacturers = models.JSONField()
    mass_kg = models.FloatField(blank=True, null=True)
    mass_lbs = models.FloatField(blank=True, null=True)
    orbit = models.CharField(max_length=100, blank=True, null=True)
    reference_system = models.CharField(max_length=100, blank=True, null=True)
    regime = models.CharField(max_length=100, blank=True, null=True)
    lifespan_years = models.IntegerField(blank=True, null=True)
    id = models.CharField(max_length=24, primary_key=True)

    class Meta:
        verbose_name = 'Payload'
        verbose_name_plural = 'Payloads'

    def __str__(self):
        return self.name
