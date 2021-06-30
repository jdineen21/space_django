import requests
import logging
import json

from pathlib import Path
from flatten_dict import flatten

from django.core import serializers
from django.db import IntegrityError
from django.utils.text import slugify
from django.conf import settings
from space_django import api

from spacex.models import Core, Crew, Dragon, Landpad, Launch, Launchpad, Payload, Rocket
from spacex.models import Image

global models

models = [
    Core,
    Crew,
    Dragon,
    Landpad,
    Launch,
    Launchpad,
    Payload,
    Rocket,
]

class Database:
    
    def update():
        logging.info('Starting Database Update')
        serialized_data = []
        setup_total = 0
        for model in models:
            setup_count = 0
            for data in api.external(model._meta.verbose_name_plural.title().lower()):
                
                if 'name' in data:
                    data['sanitized_name'] = slugify(data['name'])

                if hasattr(model, 'IMAGE_PATHS'):
                    data['images'], serialized_image_data = Image.write(model, data)
                    serialized_data.extend(serialized_image_data)

                serialized_data.append({
                    'pk': data['id'],
                    'model': 'spacex.%s' % (model.__name__.lower()),
                    'fields': data,
                })
                setup_count += 1

            logging.info('Setup %s %s objects' % (setup_count, model._meta.verbose_name.title()))
            setup_total += setup_count
        
        logging.info('Setup %s total objects for deserialization' % (setup_total))

        deserialized_count = 0
        for index, deserialized_object in enumerate(serializers.deserialize('json', json.dumps(serialized_data, indent=4), ignorenonexistent=True)):
            try:
                deserialized_object.save()
                deserialized_count += 1
            except IntegrityError as e:
                logging.error('Failed object deserialization "IntegrityError: %s at %s"' % (e, serialized_data[index]['model']))
        
        logging.info('Deserialized %s total objects' % (deserialized_count))
        logging.info('Completed Database Update')
        return True

    def purge():
        for model in models:
            model.objects.all().delete()

        logging.info('Done! Purge completed!')
        return True
