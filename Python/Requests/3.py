# https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)