
from cores.models import Cores

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def detail(request, core_serial):
    context = {
        'core': Cores.by_core_serial(core_serial),
    }
    return render(request, 'cores/detail.html', context)
