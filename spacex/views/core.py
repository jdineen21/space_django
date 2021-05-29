from django.shortcuts import render
from django.shortcuts import get_object_or_404

from spacex.models import Core

def detail(request, serial):
    context = {
        'core': get_object_or_404(Core, serial=serial),
    }
    return render(request, 'cores/detail.html', context)
