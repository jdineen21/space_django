from space_django import url_prefix

import requests

### Payloads api ###

def get_all_payloads():
    url = '%spayloads/' % (url_prefix)
    r = requests.get(url)
    payloads = r.json()

    return payloads