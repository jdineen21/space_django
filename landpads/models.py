import space_django.api

from django.db import models

class Landpads:

    def all():
        return space_django.api.external_cached('landpads/', 86400)

    def by_id(id):
        url_affix = 'landpads/%s/' % id
        return space_django.api.external_cached(url_affix, 86400)
