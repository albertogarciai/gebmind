import pandas as pd
import folium

df = pd.read_csv("locales_todos.csv")
df = df.dropna(subset=['latitud', 'longitud'])

mapa = folium.Map(location=[df['latitud'].mean(), df['longitud'].mean()], zoom_start=13)

for _, row in df.iterrows():
    popup_text = f"""
    <b>{row['nombre']}</b><br>
    Dirección: {row['direccion']}<br>
    Rating: {row['puntuacion_media']} ({row['numero_reviews']} reseñas)<br>
    Tipo: {row['tipo_negocio']}
    """
    folium.Marker(
        location=[row['latitud'], row['longitud']],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=row['nombre']
    ).add_to(mapa)

mapa.save("mapa_locales.html")
print("✅ Mapa interactivo generado en mapa_locales.html")
