import inspect
import json
import sys

from django.core import serializers
from django.utils.text import slugify
from space_django import api

from spacex.models import Launch, Launchpad, Rocket


class Database:

    def update():
        models = list(
            zip(*inspect.getmembers(sys.modules[__name__], inspect.isclass)))[1][1:]

        data = []
        for model in models:
            for api_data in api.external(model._meta.verbose_name_plural.title().lower()):
                api_data['sanitized_name'] = slugify(api_data['name'])
                data.append({
                    'pk': api_data['id'],
                    'model': 'spacex.%s' % (model.__name__.lower()),
                    'fields': api_data,
                })

        deserialized_count = 0
        for deserialized_object in serializers.deserialize('json', json.dumps(data, indent=4), ignorenonexistent=True):
            deserialized_object.save()
            deserialized_count += 1

        return 'Done! Deserialized %s objects' % (deserialized_count)

    def purge():
        models = list(
            zip(*inspect.getmembers(sys.modules[__name__], inspect.isclass)))[1][1:]
        for model in models:
            model.objects.all().delete()

        return 'Done! Purge completed!'
