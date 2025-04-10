#Clean.py

from dataPackage.data import *

def clean_city_data(parsed_json):
    """Extract city name, country, and population from raw JSON data."""
    clean_data = []

    for city in parsed_json['data']:
        name = city.get('name')
        country = city.get('country')
        latitude = city.get('latitude')
        clean_data.append({
            'name': name,
            'country': country,
            'latitude': latitude
        })

    return clean_data

def save_to_json(data, filename='cleaned_cities.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Cleaned data saved to {filename}")