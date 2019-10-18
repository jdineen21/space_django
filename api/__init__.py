import requests
import datetime

### Launches ###

def get_all_launches():
    url = 'https://api.spacexdata.com/v3/launches/'
    r = requests.get(url)
    launches_json = r.json()

    # Add datetime value to each dictionary in list
    for i in range(len(launches_json)):
        launch_datetime = datetime.datetime.fromtimestamp(launches_json[i]['launch_date_unix'])
        launches_json[i]['launch_datetime'] = launch_datetime

    return launches_json[::-1]

def get_past_launches():
    url = 'https://api.spacexdata.com/v3/launches/past/'
    r = requests.get(url)
    launches_json = r.json()

    # Add datetime value to each dictionary in list
    for i in range(len(launches_json)):
        launch_datetime = datetime.datetime.fromtimestamp(launches_json[i]['launch_date_unix'])
        launches_json[i]['launch_datetime'] = launch_datetime

    return launches_json[::-1]

def get_upcoming_launches():
    url = 'https://api.spacexdata.com/v3/launches/upcoming/'
    r = requests.get(url)
    launches_json = r.json()

    # Add datetime value to each dictionary in list
    for i in range(len(launches_json)):
        launch_datetime = datetime.datetime.fromtimestamp(launches_json[i]['launch_date_unix'])
        launches_json[i]['launch_datetime'] = launch_datetime

    return launches_json[::-1]

def get_launch_by_flight_number(flight_number):
    url = 'https://api.spacexdata.com/v3/launches/%s/' % (flight_number)
    r = requests.get(url)
    launch_json = r.json()
    
    # Add datetime value to dictionary
    launch_datetime = datetime.datetime.fromtimestamp(launch_json['launch_date_unix'])
    launch_json['launch_datetime'] = launch_datetime

    return launch_json

### Launchpads ###

def get_launchpads():
    url = 'https://api.spacexdata.com/v3/launchpads/'
    r = requests.get(url)
    return r.json()

def get_launchpad_by_site_id(site_id):
    url = 'https://api.spacexdata.com/v3/launchpads/%s/' % (site_id)
    r = requests.get(url)
    return r.json()