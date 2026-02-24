import re
import pandas as pd

i = 1

product_names = []
product_links = []
product_descr = []

while i < 17:
    with open("kana/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<h1 class="product_title entry-title">\s+(.+)\s+<\/h1>', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<div class="woocommerce-product-details__short-description">\s+<p>\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+', text)
    match_link = re.findall(
        r'<link href="(.+)" rel="canonical">', text)

    product_names.append(match_name)
    product_links.append(match_link)
    product_descr.append(match_desc)

    i += 1

    match_name = ''
    match_desc = ''
    match_link = ''

print("All 16 Product Name, Links, and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr, 
                  'Enlace': product_links
                  })

df.to_csv('kana/excel_kana.csv', index=False)

print("Spreadsheet with columns, 'Producto', 'Descripcion', and 'Enlace' Successfully Written")
