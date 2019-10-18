
import api

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'launches/index.html')

def detail(request, flight_number):
    launch_json = api.get_launch_by_flight_number(flight_number)
    launchpad_json = api.get_launchpad_by_site_id(launch_json['launch_site']['site_id'])
    
    context = {
        'launch': launch_json, 
        'launchpad': launchpad_json,
    }
    return render(request, 'launches/detail.html', context)

def upcoming(request):
    context = {
        'upcoming_launches': api.get_upcoming_launches(),
    }
    return render(request, 'launches/upcoming.html', context)