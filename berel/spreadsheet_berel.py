import re
import pandas as pd

i = 1

product_names = []
product_links = []
product_descr = []
product_car = []

while i < 120:
    with open("berel/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<h1 class="product_title entry-title">\s+(.*)\s+<\/h1>', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<h4>\s*<strong>\s*DESCRIPCI.*\s*<\/strong>\s*<\/h4>\s*.*\s*<p>\s*(.*)\s*<\/p>', text)
    match_car = re.findall(
        r'<strong>\s+CARACTER.+\s+<\/strong>\s+<\/p>\s+<ul.+\s+<li>\s+<p.+\s+(.+)\s+<\/p>\s+<\/li>\s+<li>\s+<p.+\s+(.+)\s+<\/p>\s+<\/li>\s+<li>\s+<p.+\s+(.+)', text)
    match_link = re.findall(
        r'link href="(.+)" rel="canonical', text)

    product_names.append(match_name)
    product_links.append(match_link)
    product_descr.append(match_desc)
    product_car.append(match_car)

    i += 1

    match_name = ''
    match_desc = ''
    match_link = ''
    match_car = ''

print("All 498 Product Name, Links, and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr, 
                  'Caracteristicas': product_car, 
                  'Enlace': product_links
                  })

df.to_csv('berel/excel_berel.csv', index=False)

print("Spreadsheet with columns, 'Producto', 'Descripcion', and 'Enlace' Successfully Written")
