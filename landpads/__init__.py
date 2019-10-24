import requests
import datetime

### Landpads api ###

def get_landing_pad_by_id(id):
    url = 'https://api.spacexdata.com/v3/landpads/%s/' % (id.upper())
    r = requests.get(url)
    landpad_json = r.json()

    return landpad_json