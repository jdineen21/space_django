import requests
import logging
import json

from pathlib import Path
from flatten_dict import flatten

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

    def write_image(url, choice):
        response = requests.get(url)
        filename = Path(url).name

        with open('media/%s' % (filename), 'wb') as file:
            file.write(response.content)

        return Image.objects.update_or_create(type=choice, source=url, image=filename)

    def testing():
        api_data = api.external('launches/5eb87d23ffd86e000604b36e')
        
        if hasattr(Launch, 'IMAGE_PATHS'):
            image_objects = []
            for choice, key in Launch.IMAGE_PATHS:
                image_urls = flatten(api_data, reducer='dot')[key]
                if isinstance(image_urls, list):
                    for url in image_urls:
                        image_objects.append(Database.write_image(url, choice))
                else:
                    image_objects.append(Database.write_image(image_urls, choice))

        logging.debug(image_objects)

        return True
    
    def update():
        logging.info('Starting Database Update')
        data = []
        setup_total = 0
        for model in models:
            setup_count = 0
            for api_data in api.external(model._meta.verbose_name_plural.title().lower()):
                if 'name' in api_data:
                    api_data['sanitized_name'] = slugify(api_data['name'])

                if hasattr(model, 'IMAGE_PATHS'):
                    api_data['images'] = []
                    for choice, key in model.IMAGE_PATHS:
                        image_sources = flatten(api_data, reducer='dot')[key]
                        if isinstance(image_sources, str):
                            image_sources = image_sources.split()

                        if image_sources is not None:
                            for url in list(image_sources):
                                image, etag = Image.write(url)
                                data.append({
                                    'pk': url,
                                    'model': 'spacex.image',
                                    'fields': {
                                        'type': choice, 
                                        'source': url,
                                        'etag': etag,
                                        'image': image,
                                    },
                                })
                                api_data['images'].append(url)

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
                logging.error('Failed object deserialization "IntegrityError: %s at %s %s"' % (e, data[index]['model'], data[index]['fields']['id']))
        
        logging.info('Deserialized %s total objects' % (deserialized_count))
        logging.info('Completed Database Update')
        return True

    def purge():
        for model in models:
            model.objects.all().delete()

        logging.info('Done! Purge completed!')
        return True
