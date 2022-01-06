from django.shortcuts import render
from django.shortcuts import get_object_or_404

from spacex.models import Dragon

def detail(request, sanitized_name):
    context = {
        'dragon': get_object_or_404(Dragon, sanitized_name=sanitized_name),
    }
    return render(request, 'dragons/detail.html', context)
