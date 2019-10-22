import launches

from django.shortcuts import render

def index(request):
    upcoming_launches = launches.get_upcoming_launches()

    context = {
        'upcoming_launches': upcoming_launches[:5],
    }
    return render(request, 'home/index.html', context)
