import requests

### Missions api ###

def get_mission_by_mission_id(mission_id):
    url = 'https://api.spacexdata.com/v3/missions/%s/' % (mission_id)
    r = requests.get(url)
    mission = r.json()

    return mission