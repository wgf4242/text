import requests
import json

host = "http://httpbin.org/"
endpoint = "post"
url = ''.join([host,endpoint])
data = {'key1':'value1','key2':'value2'}

r = requests.post(url,data=data)
#response = r.json()
print (r.text)