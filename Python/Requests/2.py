import os
import requests
from dotenv import load_dotenv
load_dotenv() 

# Create a session object
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/allen')
r = s.get('https://httpbin.org/cookies')
print("\n",r.json()['cookies'])

api=os.getenv('API_KEY')
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid={}'.format(api))
print(r.json())
r.close()