
# 🗺️ Geolocalización y Análisis de Negocios con Google Maps API

Este proyecto permite consultar, procesar y visualizar negocios en la ciudad de Madrid utilizando datos reales georreferenciados a través de la API de Google Places y mapas enriquecidos con `Folium`, `GeoPandas` y `branca`.

---

## 🚀 Funcionalidades principales

- Extracción de negocios por tipo y código postal.
- Limpieza y procesamiento de datos con categorización.
- Mapas interactivos:
  - Mapa de calor (densidad por punto)
  - Nube de puntos codificada por valoración
  - Visualización por barrio con shapefile
  - Mapas con leyenda y minimapa
- Exportación a HTML para compartir o integrar en web.

---

## 📁 Estructura del proyecto

```bash
GOOGLEMAPS/
│
├── data/                      # Datos de entrada
│   ├── locales_todos.csv      # Negocios extraídos por la API
│   └── Barrios/               # Shapefile con los barrios de Madrid
│       ├── BARRIOS.shp
│       ├── BARRIOS.shx
│       ├── BARRIOS.dbf
│       ├── BARRIOS.prj
│       └── BARRIOS.cpg
│
├── notebooks/                 # Análisis interactivo
│   └── gebmind.ipynb
│
├── src/                       # Código fuente en Python
│   ├── main.py                # Scripts de extracción con Google Maps
│   ├── mapa.py                # Generador de mapas en Folium
│   └── utils.py               # Funciones de utilidad para geolocalización y limpieza
│
├── outputs/                   # Resultados generados
│   └── mapa_locales.html
│
├── .env                       # API Key de Google (no subir)
├── README.md                  # Este archivo
└── requirements.txt           # Dependencias del proyecto (opcional)
```

---

## 🧰 Requisitos

- Python 3.8+
- Entorno recomendado: Miniconda o virtualenv

### Instalación de dependencias:

```bash
pip install -r requirements.txt
```

Ejemplo de `requirements.txt`:

```txt
pandas
requests
folium
python-dotenv
geopandas
branca
```

---

## 🔐 Variables de entorno

Crea un archivo `.env` en la raíz con tu API Key de Google:

```env
GOOGLE_API_KEY=TU_API_KEY_AQUI
```

---

## 🗺️ Fuentes de datos geográficos

- [API de Google Places](https://developers.google.com/maps/documentation/places/web-service/overview)
- [Barrios de Madrid (Ayto.)](https://datos.madrid.es/egob/catalogo/300496-0-barrios-madrid)

---

## 📌 Autor y créditos

Proyecto realizado como parte del máster en inteligencia artificial con fines de análisis urbano y toma de decisiones geolocalizadas.

---
