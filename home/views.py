import launches
import random

from django.shortcuts import render

def index(request):
    sig = [4, 14, 28, 55]
    next_launch = launches.get_next_launch()
    past_launches = launches.get_past_launches()
    random_vid = 'static/base/video/orbit_wo_%s.mp4' % (random.randint(0, 12))

    significant_launches = []
    for launch in past_launches:
        if launch['flight_number'] in sig:
            significant_launches.append(launch)

    context = {
        'next_launch': next_launch,
        'significant_launches': significant_launches[:4],
        'random_vid': random_vid,
    }
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')
