
import random

from launchpads.models import Launchpad
from launches.models import Launch

from django.shortcuts import render

def detail(request, sanitized_name):
    launchpad = Launchpad.objects.get(sanitized_name=sanitized_name)
    launchpad_launches = launchpad.launch_set.all()

    context = {
        'launchpad': launchpad,
        'launchpad_launches': launchpad_launches,
    }
    return render(request, 'launchpads/detail.html', context)
