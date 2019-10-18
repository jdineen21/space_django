
import requests
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'launches/index.html')

def detail(request, flight_number):
    launch_url = 'https://api.spacexdata.com/v3/launches/%s' % (flight_number)
    launch_req = requests.get(launch_url)
    launch_json = launch_req.json()

    launchpad_url = 'https://api.spacexdata.com/v3/launchpads/%s' % (launch_json['launch_site']['site_id'])
    launchpad_req = requests.get(launchpad_url)
    launchpad_json = launchpad_req.json()
    
    #return JsonResponse(r.json(), safe=False)
    context = {'launch': launch_json, 'launchpad': launchpad_json}
    return render(request, 'launches/detail.html', context)

def upcoming(request):
    url = 'https://api.spacexdata.com/v3/launches/upcoming'
    r = requests.get(url)
    #return JsonResponse(r.json(), safe=False)
    context = {'upcoming_launches': r.json()}
    return render(request, 'launches/upcoming.html', context)