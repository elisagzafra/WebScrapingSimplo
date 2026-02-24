import re
import pandas as pd

i = 1

product_names = []
product_model = []
product_descr = []
product_links = []

while i < 484:
    with open("urrea/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<div class="titulo desktop">\s*<h4>\s*.*\s*<\/h4>\s*<h2>\s*(.+)\s*<\/h2>', text) # Regular Expression (Regex)
    match_model = re.findall(
        r'<div class="titulo desktop">\s*<h4>\s*(.*)\s*<\/h4>\s*<h2>\s*.*\s*<\/h2>', text) # Regular Expression (Regex)
    match_link = re.findall(
        r'<meta content="(.+)" property="og:url">', text)
    match_desc = re.findall(
        r'<div id="descripcion">\s*<p>\s*([\s\S]*)\s*<\/p>', text)

    product_names.append(match_name)
    product_model.append(match_model)
    product_descr.append(match_desc)
    product_links.append(match_link)

    i += 1

    match_name = ''
    match_model = ''
    match_desc = ''
    match_link = ''

print("All 154 Product Names, Links and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                   'Modelo': product_model,
                  'Descripcion': product_descr, 
                  'Link': product_links
                  })

df.to_csv('urrea/productos_urrea.csv', index=False)

print("Spreadsheet with columns, 'Producto', 'Link' and 'Descripcion' Successfully Written")
