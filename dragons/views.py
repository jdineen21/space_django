
from dragons.models import Dragons

from django.shortcuts import render

def detail(request, id):
    dragon = Dragons.by_id(id)

    context = {
        'dragon': dragon,
    }
    return render(request, 'dragons/detail.html', context)
