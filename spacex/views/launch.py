
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from spacex.models import Launch

def index(request):
    launches = Launch.objects.all()

    context = {
        'launches': launches,
    }
    return render(request, 'launches/index/all.html', context)

def detail(request, flight_number):
    launch = get_object_or_404(Launch, flight_number=flight_number)
    rocket = launch.rocket
    
    context = {
        'launch': launch,
        'rocket': rocket,
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