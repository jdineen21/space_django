import requests

### Launchpads ###

def get_launchpads():
    url = 'https://api.spacexdata.com/v3/launchpads/'
    r = requests.get(url)
    return r.json()

def get_launchpad_by_site_id(site_id):
    url = 'https://api.spacexdata.com/v3/launchpads/%s/' % (site_id)
    r = requests.get(url)
    return r.json()