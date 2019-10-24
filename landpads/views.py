import landpads

from django.shortcuts import render

def detail(request, id):
    landpad = landpads.get_landing_pad_by_id(id)

    context = {
        'landpad': landpad,
    }
    return render(request, 'landpads/detail.html', context)
