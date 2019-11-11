import landpads
import launches

from django.shortcuts import render

def detail(request, id):
    landpad = landpads.get_landpad_by_id(id)
    past_launches = launches.get_past_launches()

    past_launches_at_landpad = []
    for launch in past_launches:
        for core in launch['rocket']['first_stage']['cores']:
            if core['landing_vehicle'] == landpad['id']:
                past_launches_at_landpad.append(launch)

    context = {
        'landpad': landpad,
        'past_launches_at_landpad': past_launches_at_landpad,
    }
    return render(request, 'landpads/detail.html', context)
