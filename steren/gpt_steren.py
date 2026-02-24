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
product_information = pd.read_csv('steren/productos_steren.csv')
responses = []

# For use in a demo
# ticker = 5

for index, row in product_information.iterrows():
    # Some products do not have a description in which case they should be skipped
    if row['Categoria'] != 'Soporte TV':
        responses.append('[]')
    else:
        # Set up the prompt, in which we get an item from each column of the current row
        prompt = f"""
    Con el nombre del producto "{row['Producto']}", de la marca "Steren", y la descripcion "{row['Descripcion']}"

    Generar una descripcion nueva de 6 oraciones, en formato de parrafo, usando las siguientes palabras:
    "soporte para pantalla", "base para tv", "brazo para tv", "instalación de Simplo"

    Asegurate que sea una descripcion facil de leer, y llena de detalles.
    """

        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            # This is where the actual prompt goes
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Add the response to the list and print it to monitor the progress
        responses.append(completion.choices[0].text)
        print(completion.choices[0].text)
        # For use in a demo
        #ticker -= 1
        #if ticker == 0:
        #    break


df = pd.DataFrame({'Response': responses})
df.to_csv("steren/response.csv", index=False)