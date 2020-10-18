import space_django.api

from django.db import models

class Launchpads:

    def all():
        return space_django.api.external_cached('launchpads/', 604800)

    def by_site_id(site_id):
        url_affix = 'launchpads/%s/' % site_id
        return space_django.api.external_cached(url_affix, 604800)

class LaunchpadImage(models.Model):
    site_id = models.CharField(max_length=30)
    image_location = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Launchpad Image'
        verbose_name_plural = 'Launchpad Images'
