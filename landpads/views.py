import landpads

from django.shortcuts import render

def detail(request, id):
    landpad = landpads.get_landpad_by_id(id)

    context = {
        'landpad': landpad,
    }
    return render(request, 'landpads/detail.html', context)
