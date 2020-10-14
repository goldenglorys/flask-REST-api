import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.post(BASE + "helloworld/Steve/19")

data = [
    {"name": "SWAT", "views": 200, "likes": 10},
    {"name": "SEAL", "views": 250, "likes": 15},
    {"name": "SWOT", "views": 300, "likes": 25}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# input()

# response = requests.delete(BASE + "video/0")
# print(response)

# response2 = requests.put(BASE + "video/1", {"name": "SWAT", "views": 200, "likes": 10})
# print(response2.json())
input()
response = requests.get(BASE + "video/20")
print(response.json())
