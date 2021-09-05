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