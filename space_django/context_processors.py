import launchpads
import landpads
import rockets
import dragons

def categories_processor(request):
    all_launchpads = launchpads.get_launchpads()
    all_landpads = landpads.get_landpads()
    all_rockets = rockets.get_all_rockets()
    all_dragons = dragons.get_all_dragons()

    sidebar = {
        'launchpads': [],
        'landpads': [],
        'rockets': [],
        'dragons': [],
    }

    for launchpad in all_launchpads:
        sidebar['launchpads'].append(launchpad)
    
    for landpad in all_landpads:
        sidebar['landpads'].append(landpad)

    for rocket in all_rockets:
        sidebar['rockets'].append(rocket)
    
    for dragon in all_dragons:
        sidebar['dragons'].append(dragon)
    
    context = {
        'sidebar': sidebar,
    }
    return context