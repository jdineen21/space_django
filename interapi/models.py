from django.db import models

class Request(models.Model):
    url = models.CharField(max_length=200)
    response = models.TextField()
    timestamp = models.DateTimeField('request timestamp')
