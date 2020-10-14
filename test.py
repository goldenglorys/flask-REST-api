import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "helloworld/Steve/19")

response2 = requests.put(BASE + "video/1", {"name": "SWAT", "views": 200, "likes": 10})
print(response2.json())
input()
response2 = requests.get(BASE + "video/1")
print(response2.json())
