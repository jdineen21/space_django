from space_django import url_prefix

import requests

### Missions api ###

def get_mission_by_mission_id(mission_id):
    url = '%smissions/%s/' % (url_prefix, mission_id)
    r = requests.get(url)
    mission = r.json()

    return mission