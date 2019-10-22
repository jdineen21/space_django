import requests

from django.utils import timezone

from iterapi.models import Request

def call(url):
    response = requests.get(url)
    response_dict = response.json()

    r = Request(url=url, response=response_dict, timestamp=timezone.now())
    r.save()

    return response_dict
