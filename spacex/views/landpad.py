
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from spacex.models import Landpad

def detail(request, sanitized_name):
    landpad = get_object_or_404(Landpad, sanitized_name=sanitized_name)
    
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
