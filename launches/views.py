
import launches
import launchpads
import missions
import payloads
import rockets
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.views import defaults

def index(request):
    all_launches = launches.get_all_launches()

    context = {
        'launches': all_launches,
    }
    return render(request, 'launches/index/all.html', context)

def detail(request, flight_number):
    launches_all = launches.get_all_launches()
    launches_past = launches.get_past_launches()

    launch = None
    for launch_temp in launches_all:
        if launch_temp['flight_number'] == flight_number:
            launch = launch_temp
    
    if launch is None:
        return defaults.page_not_found(request, None)

    launchpad = launchpads.get_launchpad_by_site_id(launch['launch_site']['site_id'])
    rocket = rockets.get_rocket_by_rocket_id(launch['rocket']['rocket_id'])
    
    launches_related = []
    for launch_temp in launches_past:
        if launch_temp['mission_id'] != []:
            if launch_temp['flight_number'] != flight_number:
                if launch_temp['mission_id'] == launch['mission_id']:
                    launches_related.append(launch_temp)
    
    context = {
        'launch': launch, 
        'launchpad': launchpad,
        'rocket': rocket,
        'launches_related': launches_related[:7],
    }
    return render(request, 'launches/detail.html', context)

def next(request):
    next_launch = launches.get_next_launch()

    return detail(request, next_launch['flight_number'])

def past(request):
    past_launches = launches.get_past_launches()

    context = {
        'launches': past_launches,
    }
    return render(request, 'launches/index/past.html', context)

def upcoming(request):
    upcoming_launches = launches.get_upcoming_launches()

    context = {
        'launches': upcoming_launches,
    }
    return render(request, 'launches/index/upcoming.html', context)