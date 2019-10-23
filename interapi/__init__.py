import requests

from django.utils import timezone

#from interapi.models import Request

def call(url):
    r = requests.get(url)
    response = r.text

    #r = models.Request(url=url, response=response, timestamp=timezone.now())
    #r.save()

    return response
