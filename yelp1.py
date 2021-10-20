import requests
import json

from requests.models import Response
url = 'https://api.yelp.com/v3/businesses/search'
key = 'nononoNoKEYforYou'
headers = {
    'Authorization': 'Bearer %s' % key
    }
parameters = {'term': 'seafood', 'location':'Charlottesville, VA', 'radius': 5000, 'limit': 5}

#Making Request to the API
req = requests.get(url, params=parameters, headers=headers)

# Proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

#Print Test from Request
#json.loads(req.text)
#req.json()
search = req.json()['businesses']
for place in search:
    print('Eatery: {}'.format(place['name']))
#print(req.text)
