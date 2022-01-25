import requests
import json

res = requests.get("https://portfolio-vio.herokuapp.com/certificates/")

data = res.json()['certificates']

print(data)
