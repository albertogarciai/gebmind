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
    codigos_postales = ['28001', '28002', '28003', '28004', '28005', '28006', '28007', '28008', '28009', '28010', '28011', '28012', '28013', '28014', '28015', '28016', '28017', '28018', '28019', '28020', '28021', '28022', '28023', '28024', '28025', '28026', '28027', '28028', '28029', '28030', '28031', '28032', '28033', '28034', '28035', '28036', '28037', '28038', '28039', '28040', '28041', '28042', '28043', '28044', '28045', '28046', '28047', '28048', '28049', '28050', '28051', '28052', '28053', '28054', '28055']
    tipo = None  # o por ejemplo 'restaurant'
    procesar_codigos_postales(codigos_postales, tipo_negocio=tipo)