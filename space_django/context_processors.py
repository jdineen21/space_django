from launchpads.models import Launchpads
from landpads.models import Landpads
from rockets.models import Rockets
from dragons.models import Dragons

def categories_processor(request):
    all_launchpads = sorted(Launchpads.all(), key = lambda i:(i['status'], i['name']))
    all_landpads = sorted(Landpads.all(), key = lambda i:(i['status'], i['id']))
    all_rockets = Rockets.all()
    all_dragons = Dragons.all()
    
    context = {
        'sidebar': {
            'launchpads': all_launchpads,
            'landpads': all_landpads,
            'rockets': all_rockets,
            'dragons': all_dragons,
        },
    }
    return context