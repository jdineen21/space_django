from space_django import url_prefix

import requests

### Landpads api ###

def get_landpads():
    url = '%slandpads/' % (url_prefix)
    r = requests.get(url)
    landpads_json = r.json()

    return landpads_json

def get_landpad_by_id(id):
    url = '%slandpads/%s/' % (url_prefix, id.upper())
    r = requests.get(url)
    landpad_json = r.json()

    return landpad_json