from space_django import url_prefix

import requests
import datetime

### Launches api ###

def get_all_launches():
    url = '%slaunches/' % url_prefix
    r = requests.get(url)
    launches_json = r.json()

    # Add datetime value to each dictionary in list
    for i in range(len(launches_json)):
        launch_datetime = datetime.datetime.fromtimestamp(launches_json[i]['launch_date_unix'])
        launches_json[i]['launch_datetime'] = launch_datetime

    return launches_json[::-1]

def get_next_launch():
    url = '%slaunches/next/' % url_prefix
    r = requests.get(url)
    launch_json = r.json()

    return launch_json

def get_past_launches():
    url = '%slaunches/past/' % url_prefix
    r = requests.get(url)
    launches_json = r.json()

    # Add datetime value to each dictionary in list
    for i in range(len(launches_json)):
        launch_datetime = datetime.datetime.fromtimestamp(launches_json[i]['launch_date_unix'])
        launches_json[i]['launch_datetime'] = launch_datetime

    return launches_json[::-1]

def get_upcoming_launches():
    url = '%slaunches/upcoming/' % url_prefix
    r = requests.get(url)
    launches_json = r.json()

    # Add datetime value to each dictionary in list
    for i in range(len(launches_json)):
        launch_datetime = datetime.datetime.fromtimestamp(launches_json[i]['launch_date_unix'])
        launches_json[i]['launch_datetime'] = launch_datetime

    return launches_json

def get_launch_by_flight_number(flight_number):
    url = '%slaunches/%s/' % url_prefix, flight_number
    r = requests.get(url)
    launch_json = r.json()
    
    # Add datetime value to dictionary
    launch_datetime = datetime.datetime.fromtimestamp(launch_json['launch_date_unix'])
    launch_json['launch_datetime'] = launch_datetime

    return launch_json