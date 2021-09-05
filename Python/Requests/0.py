import os
import requests
from dotenv import load_dotenv
load_dotenv()

api=os.getenv('API_KEY')
s='http://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid={}'.format(api)
r = requests.get(s)
print(r.json())
r.close()