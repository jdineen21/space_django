
import requests
import logging

from django.core.cache import cache

url_prefix = 'https://api.spacexdata.com/v3/'

def external_cached(url_affix, cache_time):
    cache_key = url_affix
    data = cache.get(cache_key, 'has expired')
    if data == 'has expired':
        logging.info('[MISS] Data Request to %s' % cache_key)
        url = '%s%s' % (url_prefix, url_affix)
        data = requests.get(url).json()
        cache.set(cache_key, data, cache_time)
    else:
        logging.info('[HIT] Data Request to %s' % cache_key)
    
    return data
