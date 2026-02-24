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
product_information = pd.read_csv('llanodelatorre/spreadsheets/mub.csv')
responses = []

# For use in a demo
# ticker = 5

for index, row in product_information.iterrows():
    match row['Categoria']:
        case 'WC':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

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
    y es de la marca "Llano de la Torre".

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
        case 'Asiento WC':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "asiento para wc", "asiento para taza de baño", "instalación de Simplo"

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
        case 'Mueble':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "muebles para baño", "muebles para lavabo de baño","muebles para lavamanos","muebles para baño con labavo",
    "cómodas para baño","Muebles de baño","instalación de Simplo"

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
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "urinario", "instalación de Simplo"

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
    y es de la marca "Llano de la Torre".

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
        case 'Desviador':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "desviador","instalación de Simplo"

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
        

df = pd.DataFrame({'Response': responses})
df.to_csv("llanodelatorre/muebles.csv", index=False)