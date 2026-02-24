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
product_information = pd.read_csv('llanodelatorre/spreadsheets/b6.csv')
responses = []

# For use in a demo
# ticker = 5

for index, row in product_information.iterrows():
    time.sleep(10)
    match row['Categoria']:
        case 'Valvula':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "válvula de descarga", "fluxómetro", "instalación de Simplo"

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

        case 'Regadera':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

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
        case 'Percha':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "percha", "perchero", "gancho para toallas", "colgadores de toallas", "percheros de pared", 
    ""gancho","instalación de Simplo"

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
    y es de la marca "Llano de la Torre".

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
    y es de la marca "Llano de la Torre".

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
    y es de la marca "Llano de la Torre".

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
        case 'Coladera':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "desagües","rebosadero","coladera", "instalación de Simplo"

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
    y es de la marca "Llano de la Torre".

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
        case 'Agarradera':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "barra de soporte", "soporte barra ducha", "barra soporte baño", "soporte barra de ducha", "soporte de pared",
    "agarradera","instalación de Simplo"

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
    y es de la marca "Llano de la Torre".

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
    y es de la marca "Llano de la Torre".

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
    y es de la marca "Llano de la Torre".

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
        case 'Porta papel':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

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
        case 'Dispensador':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "dosificador de jabón", "despachador de jabón", "dispensador de jabón", "instalación de Simplo"

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
        case 'Cepillero':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

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
        case 'Manerales':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

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
        case 'Cespol':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "sifón","céspol", "Tubo de lavabo", "Tubo en forma de U", "instalación de Simplo"

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
        case 'Brazo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

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
        case 'Contra':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "contra push", "tapón para regadera", "instalación de Simplo"

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
        case 'Ensamble':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "ensamble para regadera","ensamble para lavabo", "instalación de Simplo"

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
        case 'Kit Accesorios':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

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
        case 'Llave':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "grifo","llave mezcladora", "instalación de Simplo"

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
    y es de la marca "Llano de la Torre".

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
    y es de la marca "Llano de la Torre".

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
        case 'Mezcladora regadera':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "mezcladora para regadera","llave mezcladora", "instalación de Simplo"

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
        case 'Porta vasos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta vaso","apoya vasos","portavasos", "instalación de Simplo"

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
        case 'Repisa':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "estante", "instalación de Simplo"

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
df.to_csv("llanodelatorre/spreadsheets/baños6.csv", index=False)