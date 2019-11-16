import launchpads
import landpads
import rockets
import dragons

def categories_processor(request):
    all_launchpads = sorted(launchpads.get_launchpads(), key = lambda i:(i['status'], i['name']))
    all_landpads = sorted(landpads.get_landpads(), key = lambda i:(i['status'], i['id']))
    all_rockets = rockets.get_all_rockets()
    all_dragons = dragons.get_all_dragons()
    
    context = {
        'sidebar': {
            'launchpads': all_launchpads,
            'landpads': all_landpads,
            'rockets': all_rockets,
            'dragons': all_dragons,
        },
    }
    return context