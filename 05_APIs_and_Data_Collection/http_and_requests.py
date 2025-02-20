import requests
import os
from PIL import Image

url = 'https://www.ibm.com'
r = requests.get(url)

# Information about the request 
print(r.status_code)

# Viewing the request body
print("request body:", r.request.body)

# Viewing the HTTP response header
header = r.headers


# Obtaining the date, content-type and enconding
header['date']
header['Content-Type']
r.encoding

# We can use the attribute text to display the HTML in the body. We can review the first 100 characters:
r.text[0:100]

# Making get request considering the new URL of the following image:
new_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

re = requests.get(new_url)
print(re.headers)
print(re.headers['Content-Type'])

# An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name

path = os.path.join(os.getcwd(), 'image.png')
print(path)

# We save the file, in order to access the body of the response we use the attribute content then save it using the open function and write method:

with open(path, 'wb') as f:
    f.write(re.content)

# View the image
Image.open(path)

# Question 1: write wget

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt' 

path = os.path.join(os.getcwd(), 'Example1.txt')
r = requests.get(url)
with open(path, 'wb') as f:
    f.write(r.content)

# Post Requests
# Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:
url_post = 'http://httpbin.org/post'
payload={"name":"Joseph","ID":"123"}
r_post = requests.post(url_post, data = payload)
print("POST request URL:",r_post.url )
print(r_post.json()['form'])