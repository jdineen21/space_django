import validators
import requests
import logging
import json

from pathlib import Path
from flatten_dict import flatten

from django.core import serializers
from django.core.files import File
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

    def testing():
        api_data = api.external('launches/5eb87d23ffd86e000604b36e')
        
        Image.IMAGE_TYPE_CHOICES

        for k, v in flatten(api_data, reducer='underscore', enumerate_types=(list,)).items():
            if isinstance(v, str):
                if validators.url(v):
                    path = Path(v)
                    if path.suffix in ['.jpg', '.png']:
                        response = requests.get(v)
                        file = open('media/%s' % (path.name), 'wb')
                        file.write(response.content)
                        file.close()
        return True

    def images():
        response = requests.get('https://images2.imgbox.com/66/d2/oVB1ofaZ_o.png')
        open('media/%s' % (response.url.split('/')[-1]), 'wb')
        print(response.url)
    
    def update():
        logging.info('Starting Database Update')
        data = []
        setup_total = 0
        for model in models:
            setup_count = 0
            for api_data in api.external(model._meta.verbose_name_plural.title().lower()):
                if 'name' in api_data:
                    api_data['sanitized_name'] = slugify(api_data['name'])
                data.append({
                    'pk': api_data['id'],
                    'model': 'spacex.%s' % (model.__name__.lower()),
                    'fields': api_data,
                })
                setup_count += 1

            logging.info('Setup %s %s objects' % (setup_count, model._meta.verbose_name.title()))
            setup_total += setup_count
        
        logging.info('Setup %s total objects for deserialization' % (setup_total))

        deserialized_count = 0
        for index, deserialized_object in enumerate(serializers.deserialize('json', json.dumps(data, indent=4), ignorenonexistent=True)):
            try:
                deserialized_object.save()
                deserialized_count += 1
            except IntegrityError as e:
                logging.error('Failed object deserialization "IntegrityError: %s at %s %s"' % (e, model._meta.verbose_name.title(), data[index]['fields']['id']))
        
        logging.info('Deserialized %s total objects' % (deserialized_count))
        logging.info('Completed Database Update')
        return True

    def purge():
        for model in models:
            model.objects.all().delete()

        logging.info('Done! Purge completed!')
        return True
