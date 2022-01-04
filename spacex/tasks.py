import functools
import logging
import json
import itertools

from django.core import serializers
from django.db import IntegrityError
from django.utils.text import slugify
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
        logging.info('Starting Database Setup')

        model_data_pairs = []
        for model in models:
            data_block = api.external(model._meta.verbose_name_plural.title().lower())
            for data in data_block:
                model_data_pairs.append([model, data])

        for model, data in model_data_pairs:
            if 'name' in data:
                data['sanitized_name'] = slugify(data['name'])
            
            if hasattr(model, 'IMAGE_PATHS'):
                data['images'], images_data = Image.write(model, data)
                image_data_pairs = [[Image, image_data] for image_data in images_data]
                model_data_pairs.extend(image_data_pairs)
        
        serialized = [{'pk': model._meta.pk.name, 'model': 'spacex.%s' % (model.__name__.lower()), 'fields': data} for model, data in model_data_pairs]
        serialized.reverse()
        print(len(serialized))

        deserialized_count = 0
        for index, deserialized_object in enumerate(serializers.deserialize('json', json.dumps(serialized, indent=4), ignorenonexistent=True)):
            try:
                deserialized_object.save()
                deserialized_count += 1
            except IntegrityError as e:
                logging.error('Failed object deserialization "IntegrityError: %s at %s id %s"' % (e, serialized[index]['model'], serialized[index]['pk']))
        logging.info('Deserialized %s total objects' % (deserialized_count))
        logging.info('Completed Database Update')
    
    def purge():
        for model in models:
            model.objects.all().delete()

        logging.info('Done! Purge completed!')
        return True
