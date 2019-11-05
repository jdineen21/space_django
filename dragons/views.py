import dragons

from django.shortcuts import render

def detail(request, id):
    dragon = dragons.get_dragon_by_id(id)

    context = {
        'dragon': dragon,
    }
    return render(request, 'dragons/detail.html', context)
