
from django.db import models

from .launchpad import Launchpad

class LaunchpadImage(models.Model):
    launchpad = models.ForeignKey(Launchpad, on_delete=models.DO_NOTHING)
    image_location = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Launchpad Image'
        verbose_name_plural = 'Launchpad Images'
    
    def __str__(self):
        return str(self.id)