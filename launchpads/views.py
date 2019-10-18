
import api

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    context = {
        'launchpads': api.get_launchpads(),
    }
    return render(request, 'launchpads/index.html', context)

def detail(request, site_id):
    launchpad = api.get_launchpad_by_site_id(site_id)

    launches = api.get_past_launches()

    context = {
        'launchpad': launchpad,
        'launches': launches,
    }
    return render(request, 'launchpads/detail.html', context)
