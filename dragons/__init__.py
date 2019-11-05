import requests
import datetime

url_prefix = 'https://api.spacexdata.com/v3/'

def get_dragon_by_id(id):
    url = '%sdragons/%s/' % (url_prefix, id)
    r = requests.get(url)
    dragon_json = r.json()

    return dragon_json