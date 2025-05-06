# 📍 Geolocalizador de Negocios por Código Postal

Este proyecto permite obtener información detallada de locales y empresas en zonas específicas, utilizando el **Google Places API**. Se consultan los negocios ubicados en uno o varios códigos postales y se guarda la información estructurada en un archivo CSV.

---

## 🚀 Características

- Consulta automatizada de locales usando Google Places API.
- Extracción de datos como:
  - Nombre del local
  - Dirección
  - Código postal
  - Puntuación media
  - Número de reseñas
  - Tipo de negocio
- Exportación directa a `locales.csv`
- Compatible con múltiples códigos postales.
- Filtro opcional por tipo de negocio (`restaurant`, `store`, etc.).
- Uso seguro de credenciales con archivo `.env`.

---

## 📂 Estructura del Proyecto

```
geolocalizador/
├── .env                 # Clave API (NO subir a repositorios públicos)
├── main.py              # Script principal de ejecución
├── utils.py             # Funciones auxiliares
├── requirements.txt     # Dependencias del proyecto
└── locales.csv          # Salida generada automáticamente
```

---

## 🔧 Instalación

1. **Clona el repositorio o copia los archivos:**

```bash
git clone https://github.com/tu-usuario/geolocalizador.git
cd geolocalizador
```

2. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

3. **Crea un archivo `.env` con tu clave de API:**

```env
GOOGLE_API_KEY=tu_clave_api
```

> Puedes obtener tu clave en [Google Cloud Console](https://console.cloud.google.com/). Asegúrate de habilitar las APIs:
> - Places API
> - Geocoding API

---

## ▶️ Uso

Edita el archivo `main.py` para incluir los códigos postales que quieras procesar:

```python
codigos_postales = ['28013', '08001', '46001']  # Madrid, Barcelona, Valencia
tipo = 'restaurant'  # o 'store', 'bar', etc. (opcional)
```

Luego, ejecuta el script:

```bash
python main.py
```

> El archivo `locales.csv` se generará automáticamente con todos los datos extraídos.

---

## 📌 Notas

- La API de Google tiene un límite gratuito de $200/mes, suficiente para pruebas.
- Si hay muchos resultados, se usa `next_page_token` para paginar adecuadamente.
- Puedes adaptar fácilmente este proyecto para integrarlo con una base de datos o frontend.
- Si no configuras tipo_negocio, se creará: locales_todos.csv
    - Si pones tipo_negocio = "restaurant" → se creará: locales_restaurant.csv

---

## 📘 Licencia

Este proyecto es parte de un trabajo académico. Uso libre con fines educativos.