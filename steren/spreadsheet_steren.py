import re
import pandas as pd

i = 1

product_names = []
product_descr = []
product_descr2 = []

while i <961:
    with open("steren/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<span class="base" data-ui-id="page-title-wrapper">\s*(.+)\s*<\/span>', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<div class="value">\s*<.+>\s*(.+)\s*<\/.+>', text)
    match_desc2 = re.findall(
        r'<div class="product attribute description">\s*<div class="value">\s*(.+)\s*<\/div>', text)

    product_names.append(match_name)
    product_descr.append(match_desc)
    product_descr2.append(match_desc2)

    i += 1

    match_name = ''
    match_desc = ''
    match_desc2 = ''

print("All 16 Product Names and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr,
                  'Descripcion2': product_descr2
                  })

df.to_csv('steren/productos_steren.csv', index=False)

print("Spreadsheet with columns, 'Producto' and 'Descripcion' Successfully Written")
