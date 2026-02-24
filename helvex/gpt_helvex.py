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
product_information = pd.read_csv('helvex/helvex6.csv')
responses = []

# For use in a demo
# ticker = 5

for index, row in product_information.iterrows():
    match row['Categoria']:
        case 'Fluxometros':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "válvula de descarga", "instalación de Simplo"

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

        case 'Regaderas':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Ganchos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Tanques':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "tanque para inodoro", "tanque de wc", "depósito para wc", "depósito para inodoro", "instalación de Simplo"

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
    y es de la marca "Helvex".

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
        case 'WC':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Toallero':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta toallas", "instalación de Simplo"

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
        case 'Jaboneras':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta jabón", "instalación de Simplo"

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
        case 'Coladeras':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "desagües", "instalación de Simplo"

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
        case 'Lavabos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Monomando lavabo':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Monomandos electronicos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "llave mezcladora electrica", "instalación de Simplo"

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
        case 'Asientos WC':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "asiento", "asiento para wc", "asiento para taza de baño", "instalación de Simplo"

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
        case 'Agarraderas':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "barra de soporte", "soporte barra ducha", "barra soporte baño", "soporte barra de ducha", "soporte de pared",
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
        case 'Espejos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Salida de tina':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Repisas':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "estantes", "instalación de Simplo"

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
    y es de la marca "Helvex".

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
        case 'Portarrollos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta rollo", "instalación de Simplo"

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
        case 'Dosificador de jabon':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

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
        case 'Portacepillos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "porta cepillos", "instalación de Simplo"

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
    y es de la marca "Helvex".

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
        case 'Monomandos hospital':
            responses.append('[]')
        case 'Destapador':
            responses.append('[]')
        case 'Valvulas':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "válvula wc", "válvulas para baño", "instalación de Simplo"

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
        case 'Céspoles':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "sifón", "Tubo de lavabo", "Tubo en forma de U", "instalación de Simplo"

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
        case 'Vasos':
            prompt = f"""

    Te voy a dar un producto y tu vas a generar una descripción para este producto.

    El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
    y es de la marca "Helvex".

    Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
    "vaso de baño", "vaso para baño", "instalación de Simplo"

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
        case '[]':
            responses.append('[]')
        




df = pd.DataFrame({'Response': responses})
df.to_csv("helvex/productos6.csv", index=False)