import requests
import logging

from pathlib import Path

from django.db import models

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
    )
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.etag

    def write(url):
        headers = requests.head(url, allow_redirects=True).headers
        filename = Path(url).name
        try:
            if Image.objects.get(source=url).etag != headers['etag']:
                logging.debug('Etag change writing image')
                Image.request(url, filename)
            else:
                logging.debug('No change keeping current image')
        except Image.DoesNotExist:
            logging.debug('No record of Image creating now')
            Image.request(url, filename)
        return filename, headers['etag']
    
    def request(url, filename):
        try:
            response = requests.get(url)
        except ConnectionError as e:
            logging.error('Failed connection "ConnectionError: %s"' % (e))

        with open('media/%s' % (filename), 'wb') as file:
            file.write(response.content)
    
    def get_images(id, model, type):
        images = []
        for o in model.objects.get(id=id).images.filter(type=type):
            images.append(o.image.url)
        if len(images) == 1:
            images = images[0]
        return images
