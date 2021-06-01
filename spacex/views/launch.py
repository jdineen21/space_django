from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404


from spacex.models import Launch

def index(request):
    launches = Launch.objects.all()

    context = {
        'launches': launches,
    }
    return render(request, 'launches/index/all.html', context)

def detail(request, page_number):
    p = Paginator(Launch.objects.all(), 1)

    try:
        page_obj = p.page(page_number)
    except EmptyPage:
        raise Http404()

    context = {
        'page_obj': page_obj,
        'launch': page_obj.object_list.first(),
        'slider_images': page_obj.object_list.first().links['flickr']['original'],
        #'launches_related': launches_related[:7],
    }
    return render(request, 'launches/detail.html', context)

def next(request):
    return detail(request, Launches.next()['id'])

def past(request):
    launches = Launch.objects.filter(upcoming=False)

    context = {
        'launches': launches,
    }
    return render(request, 'launches/index/past.html', context)

def upcoming(request):
    launches = Launch.objects.filter(upcoming=True)

    context = {
        'launches': launches,
    }
    return render(request, 'launches/index/upcoming.html', context)