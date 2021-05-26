
from spacex.models import Launchpad

from django.shortcuts import render
from django.shortcuts import get_object_or_404

def detail(request, sanitized_name):
    launchpad = get_object_or_404(Launchpad, sanitized_name=sanitized_name)
    launchpad_launches = launchpad.launch_set.all()

    context = {
        'launchpad': launchpad,
        'launchpad_launches': launchpad_launches,
    }
    return render(request, 'launchpads/detail.html', context)
