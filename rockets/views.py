
from rockets.models import Rockets
from launches.models import Launches

from django.shortcuts import render

def detail(request, rocket_id):
    rocket = Rockets.by_rocket_id(rocket_id)
    past_launches = Launches.past()

    # Recent Related Launchs
    related_launches = []
    for launch in past_launches:
        if launch['rocket']['rocket_id'] == rocket['rocket_id']:
            related_launches.append(launch)
    
    recent_related_launches = related_launches[:5]

    # Get First Launch With Matching Rocket ID
    first_launch = None
    if len(related_launches) > 0:
        first_launch = related_launches[0]

    context = {
        'rocket': rocket,
        'first_launch': first_launch,
        'recent_related_launches': recent_related_launches,
    }
    return render(request, 'rockets/detail.html', context)
