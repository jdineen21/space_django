
import requests
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, 'launches/index.html')

def detail(request, flight_number):
    url = 'https://api.spacexdata.com/v3/launches/%s' % (flight_number)
    r = requests.get(url)
    #return JsonResponse(r.json(), safe=False)
    context = {'launch': r.json()}
    return render(request, 'launches/detail.html', context)

def upcoming(request):
    url = 'https://api.spacexdata.com/v3/launches/upcoming'
    r = requests.get(url)
    #return JsonResponse(r.json(), safe=False)
    context = {'upcoming_launches': r.json()}
    return render(request, 'launches/upcoming.html', context)