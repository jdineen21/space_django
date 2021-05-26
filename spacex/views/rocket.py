
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from spacex.models import Rocket

def detail(request, id):
    rocket = get_object_or_404(Rocket, id=id)

    context = {
        'rocket': rocket,
        # 'first_launch': first_launch,
        # 'recent_related_launches': recent_related_launches,
    }
    return render(request, 'rockets/detail.html', context)
