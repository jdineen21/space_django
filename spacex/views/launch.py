import re

from django.core.paginator import EmptyPage, Paginator
from django.http import Http404
from django.shortcuts import render

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

    launch = page_obj.object_list.first()
    similar_launches = Launch.objects.filter(name__icontains=re.split(' |-', launch.name)[0]).exclude(id=launch.id).reverse()
    images = launch.images.all()
    launchpad_image = launch.launchpad.images.all().first()

    context = {
        'page_obj': page_obj,
        'launch': launch,
        'patch_images': images.filter(type='patch').first(),
        'slider_images': images.filter(type='image'),
        'similar_launches': similar_launches[:6],
        'launchpad_image': launchpad_image,
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