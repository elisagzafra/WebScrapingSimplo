import re
import pandas as pd

i = 1

product_names = []
product_links = []
product_descr = []

while i < 499:
    with open("castel/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<h2 class="single-post-title product_title entry-title" itemprop="name">\n(.+)\n', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<p class="description-style">\n(.+)\n', text)
    match_link = re.findall(
        r'<link href="(.+)" rel="canonical">', text)

    product_names.append(match_name)
    product_links.append(match_link)
    product_descr.append(match_desc)

    i += 1

    match_name = ''
    match_desc = ''
    match_link = ''

print("All 498 Product Name, Links, and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr, 
                  'Enlace': product_links})

df.to_csv('castel/productos.csv', index=False)

print("Spreadsheet with columns, 'Producto', 'Descripcion', and 'Enlace' Successfully Written")
