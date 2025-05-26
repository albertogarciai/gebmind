import pandas as pd
import numpy as np
from haversine import haversine
from sklearn.neighbors import BallTree
from sklearn.cluster import DBSCAN
import yaml

# Carga de configuración
def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)

# Función de carga y limpieza de datos def load_and_clean(config):
    df = pd.read_csv(config['data']['raw_csv'])
    # Filtrado inicial
    df = df[df['puntuacion_media'].notna() & (df['numero_reviews'] >= 3)]
    # Feature engineering básico
    df['valoracion'] = df['puntuacion_media'] * (1 - np.exp(-df['numero_reviews'] / 10))
    df['valoracion_norm'] = (
        df.groupby('categoria_negocio')['valoracion']
          .transform(lambda x: (x - x.min()) / (x.max() - x.min()))
    )
    return df

# Función de feature engineering avanzado def add_spatial_features(df):
    city_center = (40.4168, -3.7038)
    df['dist_city_center_km'] = df.apply(
        lambda r: haversine((r.latitud, r.longitud), city_center), axis=1
    )
    coords_rad = np.deg2rad(df[['latitud','longitud']].values)
    tree = BallTree(coords_rad, metric='haversine')
    df['local_density_1km'] = tree.query_radius(coords_rad, r=1/6371.0, count_only=True)
    db = DBSCAN(eps=0.5/6371.0, min_samples=10, metric='haversine')
    df['cluster_zone'] = db.fit_predict(coords_rad).astype(str)
    return df