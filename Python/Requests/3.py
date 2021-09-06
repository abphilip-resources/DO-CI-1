import json
import requests

response = requests.get('https://api.covid19api.com/summary').text
response_info = json.loads(response)        # Convert JSON to Python dictionary
print(type(response_info))                  # <class 'dict'>
country_list = []
# Print the country list with number of cases
for country_info in response_info['Countries']:
    country_list.append([country_info['Country'], country_info['TotalConfirmed']])
for z in country_list: print(z)