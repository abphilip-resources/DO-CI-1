import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=e474d2b59f05f48dd4689975c9c62471')
print(r.json())
r.close()