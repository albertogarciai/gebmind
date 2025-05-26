import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
import os

def build_and_train(proc_csv, model_path):
    df = pd.read_csv(proc_csv)
    df['clase_val'] = pd.qcut(df['valoracion_norm'], q=3, labels=['baja','media','alta'])
    feature_cols = ['latitud','longitud','categoria_negocio','dist_city_center_km',
                    'density_500m','density_1000m','density_2000m','ratio_500m_2km','cluster_zone']
    X = df[feature_cols]
    y = df['clase_val']
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    num_feats = ['latitud','longitud','dist_city_center_km','density_500m','density_1000m','density_2000m','ratio_500m_2km']
    cat_feats = ['categoria_negocio','cluster_zone']
    num_pipe = Pipeline([('scaler', StandardScaler())])
    cat_pipe = Pipeline([('onehot', OneHotEncoder(drop='first', sparse_output=False))])
    preprocessor = ColumnTransformer([('num', num_pipe, num_feats),('cat', cat_pipe, cat_feats)])
    clf = Pipeline([('prep', preprocessor),('rf', RandomForestClassifier(n_estimators=100, random_state=42))])
    clf.fit(X_tr, y_tr)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(clf, model_path)
    return clf
