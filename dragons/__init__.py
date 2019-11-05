from space_django import url_prefix

import requests

def get_all_dragons():
    url = '%sdragons/' % (url_prefix)
    r = requests.get(url)
    dragons_json = r.json()

    return dragons_json

def get_dragon_by_id(id):
    url = '%sdragons/%s/' % (url_prefix, id)
    r = requests.get(url)
    dragon_json = r.json()

    return dragon_json