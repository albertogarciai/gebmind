import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

def get_coordinates(postal_code, country='ES'):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {'address': f'{postal_code}, {country}', 'key': API_KEY}
    response = requests.get(url, params=params).json()
    if response['status'] != 'OK':
        raise ValueError(f"Error al obtener coordenadas para {postal_code}")
    location = response['results'][0]['geometry']['location']
    return location['lat'], location['lng']

def get_places(lat, lng, radius=2000, business_type=None):
    places = []
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': f'{lat},{lng}',
        'radius': radius,
        'key': API_KEY,
        'type': business_type
    }

    while True:
        res = requests.get(url, params=params).json()
        places.extend(res.get('results', []))
        if 'next_page_token' in res:
            time.sleep(2)
            params['pagetoken'] = res['next_page_token']
        else:
            break

    return places

def clean_data(places, postal_code):
    data = []
    for p in places:
        location = p.get('geometry', {}).get('location', {})
        data.append({
            'nombre': p.get('name'),
            'direccion': p.get('vicinity'),
            'codigo_postal': postal_code,
            'puntuacion_media': p.get('rating'),
            'numero_reviews': p.get('user_ratings_total'),
            'tipo_negocio': ', '.join(p.get('types', [])),
            'latitud': location.get('lat'),
            'longitud': location.get('lng')
        })
    return pd.DataFrame(data)
