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
product_information = pd.read_csv('llanodelatorre/spreadsheets/adhesivos_llano.csv')
responses = []

# For use in a demo
# ticker = 5

for index, row in product_information.iterrows():
    prompt = f"""

Te voy a dar un producto y tu vas a generar una descripción para este producto.

El nombre del producto es "{row['Producto']}", su descripción es "{row['Descripcion']}", 
y es de la marca "Llano de la Torre".

Generar una descripcion de 6 oraciones, en formato de párrafo, usando las siguientes palabras:
"pegamentos", "pegamento para porcelanato", "pegamento para cerámico", "pegazulejo", "pega azulejo"

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
df.to_csv("llanodelatorre/spreadsheets/adhe.csv", index=False)