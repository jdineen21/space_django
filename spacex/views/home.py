import random

from spacex.models import Launch

from django.shortcuts import render

def index(request):
    #next_launch = Launches.next()
    #past_launches = Launches.past()
    random_vid = 'static/assets/video/orbit_wo_%s.mp4' % (random.randint(0, 12))

    # # Get Significant Launches from DB
    # significant_launches_flight_numbers = []
    # for launch in SignificantLaunch.objects.all():
    #     significant_launches_flight_numbers.append(launch.flight_number)

    # significant_launches = []
    # for launch in past_launches:
    #     if launch['flight_number'] in significant_launches_flight_numbers:
    #         significant_launches.append(launch)

    context = {
        #'next_launch': next_launch,
        #'significant_launches': significant_launches[:4],
        'random_vid': random_vid,
    }
    return render(request, 'home/index.html', context)

def about(request):
    return render(request, 'home/about.html')
