
import requests
import logging

from django.core.cache import cache

url_prefix = 'https://api.spacexdata.com/v4/'

def external(url_affix):
    url = '%s%s' % (url_prefix, url_affix)
    data = requests.get(url).json()
    return data

def external_cached(url_affix, cache_time):
    cache_key = url_affix
    data = cache.get(cache_key, 'has expired')
    url = '%s%s' % (url_prefix, url_affix)
    if data == 'has expired':
        logging.debug('[MISS] Data Request to %s' % url)
        data = requests.get(url).json()
        cache.set(cache_key, data, cache_time)
    else:
        logging.debug('[HIT] Data Request to %s' % url)
    
    return data
