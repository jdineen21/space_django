from django.db import models
from utils.db import fields

class Request(models.Model):
    url = models.CharField(max_length=200)
    response = fields.JSONField()
    timestamp = models.DateTimeField('request timestamp')
