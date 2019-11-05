from space_django import url_prefix

import requests

### Launchpads ###

def get_launchpads():
    url = '%slaunchpads/' % (url_prefix)
    r = requests.get(url)
    return r.json()

def get_launchpad_by_site_id(site_id):
    url = '%slaunchpads/%s/' % (url_prefix, site_id)
    r = requests.get(url)
    return r.json()