#Clean.py

def clean_city_data(raw_json):
    """Extract city name, country, and population from raw JSON data."""
    clean_data = []

    for city in raw_json['data']:
        name = city.get('name')
        country = city.get('country')
        population = city.get('population')
        clean_data.append({
            'name': name,
            'country': country,
            'population': population
        })

    return clean_data

def save_to_json(data, filename='cleaned_cities.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Cleaned data saved to {filename}")