import requests
import json 

basedUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc':'0012993441012'}
response = requests.get(basedUrl, params=parameters)
print(response.url)

content = response.content
info = json.loads(content)
print(type(info))
print(info)

item = info['item']
brand = itemInfo['brand']
title = itemInfo['title']

print(brand)
print(title)