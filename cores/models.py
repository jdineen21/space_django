import space_django.api

from django.db import models

class Cores:

    def all():
        return space_django.api.external_cached('cores/', 86400)

    def upcoming():
        return space_django.api.external_cached('cores/upcoming/', 86400)

    def past():
        return space_django.api.external_cached('cores/past/', 86400)

    def by_core_serial(core_serial):
        url_affix = 'cores/%s/' % id
        return space_django.api.external_cached(url_affix, 86400)
