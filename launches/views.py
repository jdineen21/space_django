
import launches
import launchpads
import missions
import payloads

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    all_launches = launches.get_all_launches()

    context = {
        'launches': all_launches,
    }
    return render(request, 'launches/launches_all.html', context)

def detail(request, flight_number):
    launches_all = launches.get_all_launches()

    for launch_temp in launches_all:
        if launch_temp['flight_number'] == flight_number:
            launch = launch_temp

    launchpad = launchpads.get_launchpad_by_site_id(launch['launch_site']['site_id'])
    
    launches_related = []
    for launch_temp in launches_all:
        if launch_temp['flight_number'] != flight_number:
            if launch_temp['mission_id'] == launch['mission_id']:
                launches_related.append(launch_temp)
    
    context = {
        'launch': launch, 
        'launchpad': launchpad,
        'launches_related': launches_related,
    }
    return render(request, 'launches/detail.html', context)

def past(request):
    past_launches = launches.get_past_launches()

    context = {
        'launches': past_launches,
    }
    return render(request, 'launches/launches_past.html', context)

def upcoming(request):
    upcoming_launches = launches.get_upcoming_launches()

    context = {
        'launches': upcoming_launches,
    }
    return render(request, 'launches/launches_upcoming.html', context)