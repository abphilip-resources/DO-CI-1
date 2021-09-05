import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=')
print(r.json())
r.close()