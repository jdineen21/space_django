from django.db import models

class Image(models.Model):
    IMAGE_TYPE_CHOICES = [
        ('flickr', 'image'),
        ('patch', 'patch'),
    ]
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=IMAGE_TYPE_CHOICES)
    source_url = models.URLField(max_length=200)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.image.name
