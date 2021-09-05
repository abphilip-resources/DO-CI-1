import requests
from requests.auth import HTTPBasicAuth
  
# Create a session object
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/allen')
r = s.get('https://httpbin.org/cookies')
print("\n",r.json()['cookies'])


# GET Authentication with authentication error code 401
r = requests.get('https://api.github.com/notifications', 
            auth=HTTPBasicAuth('allenalvin333','pass'))
print("\nAccount exists, incorrect password: Code",r.status_code)   
r.close()

URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# location given here
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API
PARAMS = {'address':location}
  
# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
  
# extracting data in json format
print(r.json())