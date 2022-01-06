import re

from spacex.models.image import Image
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

def detail(request, flight_number):
    p = Paginator(Launch.objects.all(), 1)

    try:
        page_obj = p.page(flight_number)
    except EmptyPage:
        raise Http404()

    launch = page_obj.object_list.first()
    similar_launches = Launch.objects.filter(name__icontains=re.split(' |-', launch.name)[0]).reverse()
    images = launch.images.all()

    context = {
        'page_obj': page_obj,
        'launch': launch,
        'patch_images': images.filter(type='patch').first(),
        'slider_images': images.filter(type='image'),
        'similar_launches': similar_launches[:6],
    }
    return render(request, 'launches/detail.html', context)

def next(request):
    return detail(request, Launch.next()['id'])

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