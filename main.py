import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '097825430534'}
response = requests.get(baseUrl, params=parameters)

print(response.url)