import rockets

from django.shortcuts import render

def index(request):
    rockets_all = rockets.get_all_rockets()

    context = {
        'rockets': rockets_all,
    }
    return render(request, 'rockets/index.html', context)

def detail(request, rocket_id):
    rocket = rockets.get_rocket_by_rocket_id(rocket_id)

    context = {
        'rocket': rocket,
    }
    return render(request, 'rockets/detail.html', context)
