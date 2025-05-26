import pandas as pd
import numpy as np
from haversine import haversine
from sklearn.neighbors import BallTree
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import PolynomialFeatures
import os

def extract_overpass(output_csv, overpass_url=os.getenv('OVERPASS_API_URL')):
    import requests
    query = """[out:json][timeout:60];
area["name"="Madrid"]->.searchArea;
(
  node["shop"](area.searchArea);
  node["amenity"](area.searchArea);
);
out body;"""
    resp = requests.post(overpass_url or 'http://overpass-api.de/api/interpreter', data={'data': query})
    data = resp.json()
    records = []
    for elem in data['elements']:
        tags = elem.get('tags', {})
        records.append({
            'id_local': elem['id'],
            'latitud': elem.get('lat'),
            'longitud': elem.get('lon'),
            'nombre': tags.get('name',''),
            'categoria_tags': tags.get('shop') or tags.get('amenity') or 'desconocido'
        })
    df = pd.DataFrame(records)
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    return df

def load_and_clean(raw_csv, proc_csv):
    df = pd.read_csv(raw_csv)
    df = df[df['latitud'].notna() & df['longitud'].notna()]
    df = df[df['puntuacion_media'].notna() & (df['numero_reviews'] >= 3)]
    df['valoracion'] = df['puntuacion_media'] * (1 - np.exp(-df['numero_reviews'] / 10))
    df['valoracion_norm'] = df.groupby('categoria_negocio')['valoracion']         .transform(lambda x: (x - x.min()) / (x.max() - x.min()))
    return df

def add_spatial_features(df, proc_csv):
    city_center = (40.4168, -3.7038)
    df['dist_city_center_km'] = df.apply(lambda r: haversine((r.latitud, r.longitud), city_center), axis=1)
    coords_rad = np.deg2rad(df[['latitud','longitud']].values)
    tree = BallTree(coords_rad, metric='haversine')
    for r_km in [0.5,1.0,2.0]:
        df[f'density_{int(r_km*1000)}m'] = tree.query_radius(coords_rad, r=r_km/6371.0, count_only=True)
    df['ratio_500m_2km'] = df['density_500m'] / (df['density_2000m'] + 1)
    db = DBSCAN(eps=0.5/6371.0, min_samples=10, metric='haversine')
    df['cluster_zone'] = db.fit_predict(coords_rad).astype(str)
    poly_feats = ['dist_city_center_km','density_1000m']
    poly = PolynomialFeatures(degree=2, include_bias=False)
    arr = poly.fit_transform(df[poly_feats])
    names = poly.get_feature_names_out(poly_feats)
    poly_df = pd.DataFrame(arr, columns=names, index=df.index)
    df = pd.concat([df, poly_df], axis=1)
    os.makedirs(os.path.dirname(proc_csv), exist_ok=True)
    df.to_csv(proc_csv, index=False)
    return df
