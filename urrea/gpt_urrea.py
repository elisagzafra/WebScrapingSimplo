# This script goes through the 'productos.csv' file, row by row, and asks ChatGPT to generate a new
# Description using the popular keywords, then adds all the descriptions as a new column to the
# 'productos.csv' file, for easy access and later use

import openai
import pandas as pd
import csv
import time

# Set up the OpenAI API client
openai.api_key = "xxx"



# Set up the model, which is text completion
model_engine = "text-davinci-003"

# Get the product names and descriptions, and create the list for the new GPT-generated descriptions
product_information = pd.read_csv('urrea/u5.csv')
responses = []

# For use in a demo
# ticker = 5

for index, row in product_information.iterrows():
    # time.sleep(10)
    match row['Categoria']:
        case 'Regadera':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "regaderas para baño", "regadera de baño", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Gancho':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "percha", "perchero", "gancho para toallas", "colgadores de toallas", "percheros de pared", 
    "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Monomando regadera':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "monomandos para regadera", "llave monomando regadera", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Toallero':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta toallas","toallero", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Jabonera':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta jabón","jabonera", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Monomando lavabo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "monomandos para lavabo", "monomandos para lavamanos", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Espejo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "espejo para baño con luz", "espejo de baño", "espejo para baño", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Salida tina':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "salida de agua para tina", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Monomando cocina':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "monomandos para cocina", "llave monomando cocina", "llave para fregadero",  "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Portarrollo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea"".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta rollo","portarrollo","porta papel", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Portacepillos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta cepillos","portacepillos","cepillero", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Llaves lavabo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "maneral para baño", "llave de baño", "llaves de paso", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Otros':
            responses.append('[]')
        case 'Brazo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "brazo y chapetón","brazo para regadera", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Juego Accesorios':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "kit accesorios baño","Kit para baño", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Mezcladora cocina':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "mezcladora para cocina","llave mezcladora", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Mezcladora lavabo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "mezcladora para lavabo","llave mezcladora", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Monomando cocina':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "monomandos para cocina", "llave monomando cocina", "llave para fregadero",  "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Tanque':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "tanque para inodoro", "depósito para wc","depósito para inodoro", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Mingitorio':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "urinario","retrete","wc", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'WC':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "inodoro", "wc para baños", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Lavabo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "lavabo para baño", "lavamanos", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Kit lavabo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "Kit para baño", "paquete para baño", "lavabo para baño", "lavamanos", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)
        case 'Kit WC lavabo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Urrea".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "Kit para baño", "paquete para baño", "lavabo para baño", "lavamanos",
    "inodoro", "wc para baños", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """
            completion = openai.Completion.create(
                engine=model_engine,
                # This is where the actual prompt goes
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            responses.append(completion.choices[0].text)
            print(completion.choices[0].text)

df = pd.DataFrame({'Response': responses})
df.to_csv("urrea/response5.csv", index=False)