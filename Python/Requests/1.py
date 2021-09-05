import requests
# Syntax --> requests.OPERATION(url, params={key: value}, args)

# Print available methods   -->     print(dir(r))
# Print Guide for methods   -->     print(help(r))
# Print Headers             -->     print(r.headers)
# Print Status Code         -->     print(r.status_code)
# Print Content of Response -->     print(r.content)
# Print Text of Response    -->     print(r.text)
# Print URL of Response     -->     print(r.url)

# GET Method
r = requests.get('https://api.github.com/users/allenalvin333')
print("\nCreated at:", r.json()['created_at'])
print("HTTP Status Code:",r.status_code)           # 200 if successful
r.close()

# POST Method
r = requests.post('https://httpbin.org/post', data={'username':'allenalvin333'})
print("\nUsername:", r.json()['form'])
print("HTTP Status Code:",r.status_code)           # 200 if successful
r.close()

# PUT Method
r = requests.put('https://httpbin.org/put', data={'email':'allenbphilip@gmail.com'})
print("\nEmail:", r.json()['form']['email'])
print("HTTP Status Code:",r.status_code)           # 200 if successful
r.close()

# DELETE Method
r = requests.delete('https://httpbin.org/delete', data={'username':'allenalvin333'})
print("\nForm:", r.json()['form'])
print("HTTP Status Code:",r.status_code)           # 200 if successful
r.close()