from space_django import url_prefix

import requests

def get_dragon_by_id(id):
    url = '%sdragons/%s/' % (url_prefix, id)
    r = requests.get(url)
    dragon_json = r.json()

    return dragon_json