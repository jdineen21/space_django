import requests
import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def detail(request, site_id):
    url = 'https://api.spacexdata.com/v3/launchpads/%s' % (site_id)
    r = requests.get(url)
    #return JsonResponse(r.json(), safe=False)
    context = {'launchpad': r.json()}
    return render(request, 'launchpads/detail.html', context)
