
import launches
import launchpads

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request):
    context = {
        'launchpads': api.get_launchpads(),
    }
    return render(request, 'launchpads/index.html', context)

def detail(request, site_id):
    launchpad = launchpads.get_launchpad_by_site_id(site_id)

    past_launches = launches.get_past_launches()
    upcoming_launches = launches.get_upcoming_launches()

    context = {
        'launchpad': launchpad,
        'past_launches': past_launches,
        'upcoming_launches': upcoming_launches,
    }
    return render(request, 'launchpads/detail.html', context)
