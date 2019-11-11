from django.db import models

class LaunchpadImage(models.Model):
    site_id = models.CharField(max_length=30)
    image_location = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Launchpad Image'
        verbose_name_plural = 'Launchpad Images'
