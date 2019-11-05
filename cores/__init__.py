from space_django import url_prefix

import requests

### Cores api ###

def get_all_cores():
    url = '%scores/' % (url_prefix)
    r = requests.get(url)
    return r.json()

def get_upcoming_cores():
    url = '%scores/upcoming/' % (url_prefix)
    r = requests.get(url)
    return r.json()

def get_past_cores():
    url = '%scores/past/' % (url_prefix)
    r = requests.get(url)
    return r.json()

def get_core_by_core_serial(core_serial):
    url = '%scores/%s/' % (url_prefix, core_serial)
    r = requests.get(url)
    return r.json()