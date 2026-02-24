# 🏪 Product Scraper + AI Description Generator

Herramienta de web scraping y generación automática de descripciones de productos usando ChatGPT. Desarrollada para automatizar la catalogación de productos de múltiples marcas del sector construcción y hogar en México.

## 📦 Marcas incluidas

| Marca | Categoría |
|---|---|
| Berel | Pinturas y herramientas |
| Castel | Pisos y cerámica |
| Daltile | Pisos y revestimientos |
| Helvex | Plomería y sanitarios |
| Kana | Hogar |
| Kwikset | Cerraduras y seguridad |
| Llano de la Torre | Materiales |
| Steren | Electrónica |
| Tendenzza | Decoración |
| Terza | Pisos |
| Urrea | Herramientas |
| Vitromex | Pisos y cerámica |

## 🔧 ¿Qué hace este proyecto?

El pipeline tiene 3 etapas principales, ilustradas con el ejemplo de Castel (el mismo flujo aplica para todas las marcas):

**1. Descarga de páginas (`links_castel.py`)**
Recorre todas las páginas del catálogo de la marca, descarga el HTML de cada una, extrae los links únicos de cada producto y descarga el HTML individual de cada producto.

**2. Construcción del CSV (`spreadsheet_castel.py`)**
Parsea cada archivo HTML descargado usando expresiones regulares, extrae el nombre, descripción y enlace canonical de cada producto y genera un archivo `productos.csv` estructurado.

**3. Generación de descripciones con IA (`gpt_castel.py`)**
Lee el CSV de productos, envía cada producto a la API de OpenAI con un prompt personalizado por marca y genera una descripción optimizada en español de 6 oraciones con palabras clave relevantes para SEO, guardando el resultado en un nuevo CSV.

## 🗂 Estructura del proyecto

```
/
├── castel/
│   ├── pages/          # HTMLs de páginas del catálogo
│   ├── products/       # HTMLs individuales de productos
│   ├── productos.csv   # Datos scrapeados
│   └── pisos.csv       # Descripciones generadas por GPT
├── berel/
├── daltile/
├── ... (una carpeta por marca)
├── links_castel.py
├── spreadsheet_castel.py
└── gpt_castel.py
```

## 🚀 Uso

Instala las dependencias necesarias:
```bash
pip install openai pandas requests beautifulsoup4
```

Luego ejecuta los scripts en orden para cada marca:
```bash
python links_castel.py       # 1. Scraping
python spreadsheet_castel.py # 2. Estructurar datos
python gpt_castel.py         # 3. Generar descripciones
```

## ⚙️ Tecnologías

- **Python 3** — lenguaje principal
- **BeautifulSoup4** — parsing de HTML
- **Requests** — descarga de páginas web
- **Pandas** — manejo y exportación de datos
- **OpenAI API** — generación de descripciones con GPT

## 📝 Notas

- Los scripts de cada marca son independientes entre sí y siguen el mismo patrón.
- Las descripciones generadas por GPT están optimizadas con palabras clave específicas por categoría de producto para fines de SEO.
- Productos sin descripción original son omitidos en la generación de IA.
