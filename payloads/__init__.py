import requests

### Payloads api ###

def get_all_payloads():
    url = 'https://api.spacexdata.com/v3/payloads/'
    r = requests.get(url)
    payloads = r.json()

    return payloads