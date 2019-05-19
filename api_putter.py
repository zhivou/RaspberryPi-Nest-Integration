import json
import requests


class ApiPutter:
    redirected_to = None

    def __init__(self):
        self.access_token_cache_file = json.loads(open('token.json').read())
    #
    # Use this method for custom end points:
    #
    def update_any_value(self, device_id, key, value):
        payload = "{\"%s\": \"%s\"}" % (key, value)
        self.poster('thermostats', device_id, payload)

    # Some extra information about if statement in poster method:
    #
    # It is also a best practice to store the redirected location on a per user basis. In other words,
    # after a user signs in and a redirect is received,
    # store the firebase-apiserver03-tah01-iad01.dapi.production.nest.com:9553/
    # location and make all subsequent requests directly to this URI.
    #
    # Storing the redirected location saves time and prevents unnecessary server load.
    #
    def poster(self, device, device_id, payload):
        url = "https://developer-api.nest.com/devices/%s/%s" % (device, device_id)
        headers = {'Authorization': 'Bearer {0}'.format(self.access_token_cache_file['access_token']),
                   'Content-Type': 'application/json'}
        if ApiPutter.redirected_to is None:
            response = requests.put(url, headers=headers, data=payload, allow_redirects=False)
            if response.status_code == 307:  # indicates a redirect is needed
                ApiPutter.redirected_to = response.headers['Location']
                print('Redirected link was saved for further use cases!')
                response = requests.put(ApiPutter.redirected_to, headers=headers, data=payload, allow_redirects=False)
            else:
                print('Code was not correct Error?: ' + response.status_code)
        else:
            response = requests.put(ApiPutter.redirected_to, headers=headers, data=payload, allow_redirects=False)
        print('...........................\n' + response.text)
        print(response.status_code)
        print(response.reason)

# caller = ApiPutter()
# caller.update_any_value('F2tFuOEes_fjqfs6P1TDIDsktDB5sbk5', 'where_name', 'Living Room')
