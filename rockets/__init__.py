from space_django import url_prefix

import requests

### Rockets ###

def get_all_rockets():
    url = '%srockets/' % (url_prefix)
    r = requests.get(url)
    return r.json()

def get_rocket_by_rocket_id(rocket_id):
    url = '%srockets/%s/' % (url_prefix, rocket_id)
    r = requests.get(url)
    return r.json()