import space_django.api

from django.db import models

class Dragons:

    def all():
        return space_django.api.external_cached('dragons/', 86400)

    def by_id(id):
        url_affix = 'dragons/%s/' % id
        return space_django.api.external_cached(url_affix, 86400)
        