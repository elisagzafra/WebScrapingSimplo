# This script goes through the 'productos.csv' file, row by row, and asks ChatGPT to generate a new
# Description using the popular keywords, then adds all the descriptions as a new column to the
# 'productos.csv' file, for easy access and later use

import openai
import pandas as pd
import csv

# Set up the OpenAI API client
openai.api_key = "xxx"



# Set up the model, which is text completion
model_engine = "text-davinci-003"

# Get the product names and descriptions, and create the list for the new GPT-generated descriptions
product_information = pd.read_csv('llanodelatorre/spreadsheets/cocina_llano.csv')
responses = []

# For use in a demo
# ticker = 5

for index, row in product_information.iterrows():
    match row['Categoria']:
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
        case 'Campana':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "campana para cocina","campana extractora"

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
        case 'Fregadero':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Llano de la Torre".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "fregadero","instalación de Simplo"

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
df.to_csv("llanodelatorre/spreadsheets/coc.csv", index=False)