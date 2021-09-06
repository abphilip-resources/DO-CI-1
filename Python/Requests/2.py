import os
import csv
import json
import requests
from bs4 import BeautifulSoup

# Loading variable from .env
from dotenv import load_dotenv
load_dotenv()
api=os.getenv('API_KEY')

# API JSON on CSV
weather,locations=[],['Bengaluru','Hyderabad']
for z in range(len(locations)):
    p = {}
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(locations[z],api))
    for k1, v1 in r.json().items(): 
        if(k1=='main' or k1=='coord' or k1=='sys'):               
            for k2, v2 in v1.items(): p[k2]=v2
        else: p[k1]=v1
    weather.append(p)

# Write weather to a CSV file
with open('weather.csv', 'w', newline='') as f:
    w = csv.DictWriter(f,p.keys())
    w.writeheader()                               # Write the topics as the header
    for z in weather: w.writerow(z)               # Write each parameter to the CSV file

# HTML BeautifulSoup on CSV
r = requests.get("http://www.values.com/inspirational-quotes")
soup = BeautifulSoup(r.content, 'html5lib') 
r.close()
# print(r.content)                  --> Raw HTML Content
# print(soup.prettify())            --> Prettified HTML5 Content

# Deriving quotes from the prettified HTML5 Content
quotes=[]  
t = soup.find('div', attrs = {'id':'all_quotes'}) 
# Finding all the divs with ID = 'all_quotes'
for z in t.findAll('div', attrs = 
    {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}                                  # Create a dictionary for each quote
    quote['theme'] = z.h5.text                  # Quote's theme found at heading 5
    quote['url'] = z.a['href']
    quote['img'] = z.img['src']
    quote['lines'] = z.img['alt'].split(" #")[0]
    quote['author'] = z.img['alt'].split(" #")[1]
    quotes.append(quote)                        # Append each dictionary to the list

# Write quotes to a CSV file
with open('quotes.csv', 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()                             # Write the topics as the header
    for quote in quotes: w.writerow(quote)      # Write each quote to the CSV file