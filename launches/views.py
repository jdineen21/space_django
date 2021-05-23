
from launches.models import Launch, Launches
#from launchpads.models import Launchpads
from rockets.models import Rockets

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotFound
from django.views import defaults

def index(request):
    launches = Launch.objects.all()

    context = {
        'launches': launches,
    }
    return render(request, 'launches/index/all.html', context)

def detail(request, flight_number):
    launch = Launch.objects.get(flight_number=flight_number)
    #rocket = Rockets.by_id(launch['rocket'])
    
    context = {
        'launch': launch,
        #'rocket': rocket,
        #'launches_related': launches_related[:7],
    }
    return render(request, 'launches/detail.html', context)

def next(request):
    return detail(request, Launches.next()['id'])

def past(request):
    launches = Launch.objects.filter(upcoming=False)

    context = {
        'launches': launches,
    }
    return render(request, 'launches/index/past.html', context)

def upcoming(request):
    launches = Launch.objects.filter(upcoming=True)

    context = {
        'launches': launches,
    }
    return render(request, 'launches/index/upcoming.html', context)