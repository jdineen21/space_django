
import launches
import launchpads
import missions
import payloads
import rockets
import json

from launches.models import Launches
from launchpads.models import Launchpads
from rockets.models import Rockets

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.views import defaults

def index(request):
    context = {
        'launches': Launches.all(),
    }
    return render(request, 'launches/index/all.html', context)

def detail(request, flight_number):
    all_launches = Launches.all()
    past_launches = Launches.past()

    launch = None
    for launch_temp in all_launches:
        if launch_temp['flight_number'] == flight_number:
            launch = launch_temp
    
    if launch is None:
        return defaults.page_not_found(request, None)

    launchpad = Launchpads.by_site_id(launch['launch_site']['site_id'])
    rocket = Rockets.by_rocket_id(launch['rocket']['rocket_id'])
    
    launches_related = []
    for launch_temp in past_launches:
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
    return detail(request, Launches.next()['flight_number'])

def past(request):
    context = {
        'launches': Launches.past(),
    }
    return render(request, 'launches/index/past.html', context)

def upcoming(request):
    context = {
        'launches': Launches.upcoming(),
    }
    return render(request, 'launches/index/upcoming.html', context)