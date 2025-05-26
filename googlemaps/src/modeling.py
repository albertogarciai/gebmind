import joblib
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import yaml

# Cargar configuración
def load_config(path: str) -> dict:
    # ... mismo que preprocessing.py
    pass

# Pipeline básico def build_pipeline(config):
    num_feats = ['latitud','longitud','dist_city_center_km','local_density_1km']
    cat_feats = ['categoria_negocio','cluster_zone']

    num_pipe = Pipeline([('scaler', StandardScaler())])
    cat_pipe = Pipeline([('onehot', OneHotEncoder(drop='first', sparse_output=False))])

    preprocessor = ColumnTransformer([
        ('num', num_pipe, num_feats),
        ('cat', cat_pipe, cat_feats),
    ])
    rf_cfg = config['model']['rf']
    pipeline = Pipeline([
        ('prep', preprocessor),
        ('rf', RandomForestClassifier(
            n_estimators=rf_cfg['n_estimators'],
            random_state=rf_cfg['random_state']
        ))
    ])
    return pipeline

# Entrenamiento y evaluación def train_and_evaluate(df, config):
    X = df[num_feats + cat_feats]
    y = df['clase_val']
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y,
        test_size=config['model']['cv']['test_size'],
        stratify=y,
        random_state=config['model']['rf']['random_state']
    )
    pipeline = build_pipeline(config)
    pipeline.fit(X_tr, y_tr)
    # Evaluación ...
    joblib.dump(pipeline, 'models/rf_classifier.pkl')