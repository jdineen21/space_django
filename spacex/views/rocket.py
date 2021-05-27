
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from spacex.models import Rocket

def detail(request, sanitized_name):
    rocket = get_object_or_404(Rocket, sanitized_name=sanitized_name)

    context = {
        'rocket': rocket,
        # 'first_launch': first_launch,
        # 'recent_related_launches': recent_related_launches,
    }
    return render(request, 'rockets/detail.html', context)
