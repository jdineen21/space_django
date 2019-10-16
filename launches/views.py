
import requests
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse('Launches!')

def upcoming(request):
    url = 'https://api.spacexdata.com/v3/launches/upcoming'
    r = requests.get(url)
    #return JsonResponse(r.json(), safe=False)
    context = {'upcoming_launches': r.json()}
    return render(request, 'launches/upcoming.html', context)