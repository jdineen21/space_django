import space_django.api

from django.db import models

class Rockets:

    def all():
        return space_django.api.external_cached('rockets/', 86400)

    def by_id(id):
        url_affix = 'rockets/%s/' % id
        return space_django.api.external_cached(url_affix, 86400)
