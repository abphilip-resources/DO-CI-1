import requests

r = requests.get('https://www.google.com/search?q=hello')
# Print available methods   -->     print(dir(r))
# Print Guide for methods   -->     print(help(r))
# Print Headers             -->     print(r.headers)
# Print Status Code         -->     print(r.status_code)
# Print Content of Response -->     print(r.content)
# Print Text of Response    -->     print(r.text)
# Print URL of Response     -->     print(r.url)
 
# 200 when we get a response
print(r.status_code) 