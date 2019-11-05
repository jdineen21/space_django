from space_django import url_prefix

import requests

### Landpads api ###

def get_landing_pad_by_id(id):
    url = '%slandpads/%s/' % (url_prefix, id.upper())
    r = requests.get(url)
    landpad_json = r.json()

    return landpad_json