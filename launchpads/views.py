
import random

import launches
import launchpads

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from .models import LaunchpadImage

def detail(request, site_id):
    launchpad = launchpads.get_launchpad_by_site_id(site_id)

    past_launches = launches.get_past_launches()
    upcoming_launches = launches.get_upcoming_launches()

    past_launches_at_site = []
    for launch in past_launches:
        if launch['launch_site']['site_id'] == launchpad['site_id']:
            past_launches_at_site.append(launch)

    upcoming_launches_at_site = []
    for launch in upcoming_launches:
        if launch['launch_site']['site_id'] == launchpad['site_id']:
            upcoming_launches_at_site.append(launch)

    launchpad_image = None
    for row in LaunchpadImage.objects.all():
        if row.site_id == site_id:
            launchpad_image = row.image_location

    context = {
        'launchpad': launchpad,
        'past_launches_at_site': past_launches_at_site[:14],
        'upcoming_launches_at_site': upcoming_launches_at_site[:5],
        'launchpad_img': launchpad_image,
    }
    return render(request, 'launchpads/detail.html', context)
