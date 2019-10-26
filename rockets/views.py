import rockets
import launches
import json

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    rockets_all = rockets.get_all_rockets()

    context = {
        'rockets': rockets_all,
    }
    return render(request, 'rockets/index.html', context)

def detail(request, rocket_id):
    rocket = rockets.get_rocket_by_rocket_id(rocket_id)
    launches_all = launches.get_past_launches()

    launches_all_by_rocket_id = []
    for launch in launches_all:
        if launch['rocket']['rocket_id'] == rocket_id:
            launches_all_by_rocket_id.append(launch)

    context = {
        'rocket': rocket,
        'launch': launches_all_by_rocket_id[0],
        'launches': launches_all_by_rocket_id,
    }
    return render(request, 'rockets/detail.html', context)
