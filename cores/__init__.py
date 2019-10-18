import requests

### Cores api ###

def get_all_cores():
    url = 'https://api.spacexdata.com/v3/cores/'
    r = requests.get(url)
    return r.json()

def get_upcoming_cores():
    url = 'https://api.spacexdata.com/v3/cores/upcoming/'
    r = requests.get(url)
    return r.json()

def get_past_cores():
    url = 'https://api.spacexdata.com/v3/cores/past/'
    r = requests.get(url)
    return r.json()

def get_core_by_core_serial(core_serial):
    url = 'https://api.spacexdata.com/v3/cores/%s/' % (core_serial)
    r = requests.get(url)
    return r.json()