import launches
import random

from django.shortcuts import render

def index(request):
    upcoming_launches = launches.get_upcoming_launches()
    random_vid = 'static/base/video/orbit_wo_%s.mp4' % (random.randint(0, 12))

    context = {
        'upcoming_launches': upcoming_launches[:5],
        'random_vid': random_vid,
    }
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')
