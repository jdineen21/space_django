import requests

### Rockets ###

def get_all_rockets():
    url = 'https://api.spacexdata.com/v3/rockets/'
    r = requests.get(url)
    return r.json()

def get_rocket_by_rocket_id(rocket_id):
    url = 'https://api.spacexdata.com/v3/rockets/%s/' % (rocket_id)
    r = requests.get(url)
    return r.json()