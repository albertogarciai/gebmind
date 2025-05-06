from utils import get_coordinates, get_places, clean_data
import pandas as pd

def procesar_codigos_postales(codigos, tipo_negocio=None):
    todos_los_locales = pd.DataFrame()

    for cp in codigos:
        try:
            lat, lng = get_coordinates(cp)
            lugares = get_places(lat, lng, business_type=tipo_negocio)
            df = clean_data(lugares, cp)
            todos_los_locales = pd.concat([todos_los_locales, df], ignore_index=True)
            print(f"✅ {len(df)} locales encontrados en {cp}")
        except Exception as e:
            print(f"⚠️ Error con código postal {cp}: {e}")

    # Si se especifica tipo de negocio, úsalo en el nombre del archivo
    nombre_tipo = tipo_negocio if tipo_negocio else "todos"
    output_file = f"locales_{nombre_tipo}.csv"

    todos_los_locales.to_csv(output_file, index=False)
    print(f"\n✅ Archivo '{output_file}' generado exitosamente.")

if __name__ == '__main__':
    codigos_postales = ['28004', '28005', '28012', '28013', '28014', '28015']
    tipo = None  # o por ejemplo 'restaurant'
    procesar_codigos_postales(codigos_postales, tipo_negocio=tipo)