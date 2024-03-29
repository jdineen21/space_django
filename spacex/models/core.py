from django.db import models

from .launch import Launch

class Core(models.Model):
    block = models.IntegerField(blank=True, null=True)
    reuse_count = models.IntegerField(blank=True, null=True)
    rtls_attempts = models.IntegerField(blank=True, null=True)
    rtls_landings = models.IntegerField(blank=True, null=True)
    asds_attempts = models.IntegerField(blank=True, null=True)
    asds_landings = models.IntegerField(blank=True, null=True)
    last_update = models.TextField(blank=True, null=True)
    launches = models.ManyToManyField(Launch)
    serial = models.CharField(max_length=5)
    status = models.CharField(max_length=100)
    id = models.CharField(max_length=24, primary_key=True)

    class Meta:
        verbose_name = 'Core'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.serial
