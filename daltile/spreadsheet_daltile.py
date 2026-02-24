import pandas as pd
import re
import time


i = 1

product_col= []
product_desc = []
product_desc1 = []
product_desc2 = []

while i < 252:
    with open("daltile/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_col=re.findall(
        r'<div class="name_serie_product">\s+<div>\s+(.*)\s+<\/div>',text)
    match_desc = re.findall(
        r'<div class="content_technical_information">\s*<table>\s*<tr>\s*<td>\s*(.*)\s*<\/td>\s*<td>\s*<\/td>\s*<\/tr>\s*<\/table>', text)  
    match_desc1 = re.findall(
        r'<td class="interlineado-20">\s*<br\/>\s*<br\/>\s*<br\/>\s*(.*)\s*<\/td>\s*<\/tr>\s*<\/table>', text)  
    match_desc2 = re.findall(
        r'<td class="interlineado-20">\s*<br\/>\s*<br\/>\s*<br\/>\s*(.*)\s*<br\/>\s*(.*).\s*<br\/>\s*(.*)\s*<\/td>', text)  
    
    product_col.append(match_col)
    product_desc.append(match_desc)
    product_desc1.append(match_desc1)
    product_desc2.append(match_desc2)

    i += 1

    match_col = ''
    match_desc = ''
    match_desc1 = ''
    match_desc2 = ''

print("All 251 Product Names and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Colección': product_col,
                   'Descripcion': product_desc,
                   'Descripcion2': product_desc1,
                   'Descripcion3': product_desc2
                   })

df.to_csv('daltile/productos.csv', index=False)

print("Spreadsheet with columns, 'Producto', 'Descripcion', and 'Enlace' Successfully Written")
