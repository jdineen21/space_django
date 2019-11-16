
import random

import launches
import launchpads

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views import defaults

from .models import LaunchpadImage

def detail(request, site_id):
    all_launchpads = launchpads.get_launchpads()

    past_launches = launches.get_past_launches()
    upcoming_launches = launches.get_upcoming_launches()

    launchpad = None
    for launchpad_temp in all_launchpads:
        if launchpad_temp['site_id'] == site_id:
            launchpad = launchpad_temp
    
    if launchpad is None:
        return defaults.page_not_found(request, None)

    past_launches_at_site = []
    for launch in past_launches:
        if launch['launch_site']['site_id'] == launchpad['site_id']:
            past_launches_at_site.append(launch)

    upcoming_launches_at_site = []
    for launch in upcoming_launches:
        if launch['launch_site']['site_id'] == launchpad['site_id']:
            upcoming_launches_at_site.append(launch)

    launchpad_images = []
    for launchpad_image in LaunchpadImage.objects.filter(site_id=site_id).values_list('image_location', flat=True):
        launchpad_images.append(launchpad_image)
    print((launchpad_images))

    context = {
        'launchpad': launchpad,
        'past_launches_at_site': past_launches_at_site[:14],
        'upcoming_launches_at_site': upcoming_launches_at_site[:5],
        'launchpad_imgs': launchpad_images,
    }
    return render(request, 'launchpads/detail.html', context)
