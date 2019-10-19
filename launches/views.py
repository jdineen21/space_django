
import launches
import launchpads

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    all_launches = launches.get_all_launches()

    context = {
        'launches': all_launches,
    }
    return render(request, 'launches/launches_all.html', context)

def detail(request, flight_number):
    launch = launches.get_launch_by_flight_number(flight_number)
    launchpad = launchpads.get_launchpad_by_site_id(launch['launch_site']['site_id'])
    
    context = {
        'launch': launch, 
        'launchpad': launchpad,
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