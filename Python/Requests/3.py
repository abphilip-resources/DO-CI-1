import os
import requests
from dotenv import load_dotenv
load_dotenv()

api=os.getenv('API_KEY')
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid={}'.format(api))
print(r.json())
r.close()

