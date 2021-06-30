import requests
import logging

from pathlib import Path
from flatten_dict import flatten

from django.db import models
from django.conf import settings

def image_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.model.split('.')[-1], filename)

class Image(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('patch', 'Patch'),
        ('image', 'Image'),
        ('portrait', 'Portrait'),
    ]
    name = models.CharField(max_length=100)
    source = models.URLField(primary_key=True, max_length=200)
    type = models.CharField(max_length=10, choices=IMAGE_TYPE_CHOICES)
    etag = models.CharField(max_length=100)
    image = models.ImageField(
        height_field='height',
        width_field='width',
        upload_to=image_directory_path,
    )
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.name

    def write(model, data):
        serialized_data = []
        for choice, key in model.IMAGE_PATHS:
            path = Path(model.__name__.lower(), choice)
            path.mkdir(parents=True, exist_ok=True)

            image_sources = flatten(data, reducer='dot')[key]
            if isinstance(image_sources, str):
                image_sources = [image_sources]

            if isinstance(image_sources, list):
                for index, url in enumerate(list(image_sources)):
                    if len(image_sources) == 1:
                        filename = '%s%s' % (data['sanitized_name'], Path(url).suffix)
                    else:
                        filename = '%s-%s%s' % (data['sanitized_name'], index+1, Path(url).suffix)
                    
                    filepath = Path(path, filename)
                    
                    etag = Image.write_to_disk(filepath, url)
                    serialized_data.append({
                        'pk': filename,
                        'model': 'spacex.image',
                        'fields': {
                            'name': filename,
                            'source': url,
                            'type': choice,
                            'etag': etag,
                            'image': str(filepath),
                        },
                    })
        return image_sources, serialized_data

    def write_to_disk(filepath, url):
        headers = requests.head(url, allow_redirects=True).headers
        # try:
        #     if Image.objects.get(source=url).etag != headers['etag']:
        #         logging.debug('Etag change writing image %s/%s' % (str(filepath)))
        #         Image.download_to_disk(filepath, url)
        # except Image.DoesNotExist:
        #     Image.download_to_disk(filepath, url)
        return headers['etag']
    
    def download_to_disk(filepath, url):
        try:
            response = requests.get(url)
        except ConnectionError as e:
            logging.error('Failed connection "ConnectionError: %s"' % (e))

        with open(str(filepath), 'wb') as file:
            file.write(response.content)
