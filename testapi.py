import requests
import json

res = requests.get("http://portfolio-vio.herokuapp.com/projects/")

data = res.json()["projects"]

print(len(data))
