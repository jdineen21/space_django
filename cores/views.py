
import api

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def detail(request, core_serial):
    context = {
        'core': api.get_core_by_core_serial(core_serial),
    }
    return render(request, 'cores/detail.html', context)
