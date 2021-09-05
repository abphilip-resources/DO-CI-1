import requests
# requests.OPERATION(url, params={key: value}, args)

# Print available methods   -->     print(dir(r))
# Print Guide for methods   -->     print(help(r))
# Print Headers             -->     print(r.headers)
# Print Status Code         -->     print(r.status_code)
# Print Content of Response -->     print(r.content)
# Print Text of Response    -->     print(r.text)
# Print URL of Response     -->     print(r.url)

# GET Method
r = requests.get('https://api.github.com/users/allenalvin333')
print("Followers @Github:", r.json()['followers'])
print("HTTP Status Code:",r.status_code)           # 200 when we get a response
r.close()

# POST Method
r = requests.post('https://httpbin.org/post', data ={'key':'value'})
print("HTTP Status Code:",r.status_code)           # 200 when we get a response
r.close()