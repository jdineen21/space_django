
from landpads.models import Landpads
from launches.models import Launches

from django.shortcuts import render
from django.views import defaults

def detail(request, id):
    all_landpads = Landpads.all()
    # past_launches = Launches.past()

    landpad = None
    for landpad_temp in all_landpads:
        if landpad_temp['id'] == id:
            landpad = landpad_temp
    
    if landpad is None:
        return defaults.page_not_found(request, None)

    # past_launches_at_landpad = []
    # for launch in past_launches:
    #     for core in launch['rocket']['first_stage']['cores']:
    #         if core['landing_vehicle'] == landpad['id']:
    #             past_launches_at_landpad.append(launch)

    context = {
        'landpad': landpad,
        # 'past_launches_at_landpad': past_launches_at_landpad,
    }
    return render(request, 'landpads/detail.html', context)
