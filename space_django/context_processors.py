from launchpads.models import Launchpad
from landpads.models import Landpads
from rockets.models import Rockets
from dragons.models import Dragons

def categories_processor(request):
    launchpads = Launchpad.objects.values('name', 'sanitized_name')
    all_landpads = sorted(Landpads.all(), key = lambda i:(i['status'], i['id']))
    all_rockets = Rockets.all()
    all_dragons = Dragons.all()
    
    context = {
        'sidebar': {
            'launchpads': launchpads,
            'landpads': all_landpads,
            'rockets': all_rockets,
            'dragons': all_dragons,
        },
    }
    return context