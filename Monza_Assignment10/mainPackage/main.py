# main.py
import json
import requests

response = requests.get('https://wft-geo-db.p.rapidapi.com/v1/geo/cities?limit=100&sort=-population', 
                        headers={
                            'X-RapidAPI-Key': '4cc88cdf7cmshf7b29940764088ap104c7ajsnb09745931509',
                            'X-RapidAPI-Host': 'wft-geo-db.p.rapidapi.com'})

json_string = response.content

parsed_json = json.loads(json_string) # Now we have a python dictionary

total = int(parsed_json['metadata']['totalCount']) # The number of cities that were returned

for city in parsed_json['data']:
    print(city)


