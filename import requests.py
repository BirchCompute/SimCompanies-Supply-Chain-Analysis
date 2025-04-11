import requests
import json

def getResource(n):
    return requests.get("https://api.simcotools.com/v1/realms/0/resources/" + str(n)).json()

data = {}
for i in range(155):
    data[i] = getResource(i)

print(data)

with open("dataFile.json", mode = "w", encoding = "utf8") as file:
    json.dump(data, file)