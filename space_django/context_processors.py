from spacex.models import Launchpad
from spacex.models import Landpad
from spacex.models import Rocket
from spacex.models import Dragon

def categories_processor(request):
    launchpads = Launchpad.objects.values('name', 'sanitized_name')
    all_landpads = Landpad.objects.all()
    all_rockets = Rocket.objects.all()
    all_dragons = Dragon.objects.all()
    
    context = {
        'sidebar': {
            'launchpads': launchpads,
            'landpads': all_landpads,
            'rockets': all_rockets,
            'dragons': all_dragons,
        },
    }
    return context