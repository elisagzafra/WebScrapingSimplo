import re
import pandas as pd

i = 1

product_names = []
product_descr = []
product_descr2 = []
product_img = []
product_sku = []

while i < 442:
    with open("helvex/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<span class="base" data-ui-id="page-title-wrapper" itemprop="name">\s+(.+)\s+<\/span>', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<div class="value" itemprop="description">\s+<p>\s+(.*)\s+<\/p>', text)
    match_desc2 = re.findall(
        r'<div class="value" itemprop="description">\s*(.+)\s*<\/div>', text)
    match_img = re.findall(
        r'<img alt="main product photo" class="gallery-placeholder__image" src="(.*)">\s*<\/img>', text)
    match_sku = re.findall(
        r'<div class="value" itemprop="modelo">\s*(.*)\s*', text)

    product_names.append(match_name)
    product_descr.append(match_desc)
    product_descr2.append(match_desc2)
    product_img.append(match_img)
    product_sku.append(match_sku)

    i += 1

    match_name = ''
    match_desc = ''
    match_desc2 = ''
    match_img = ''
    match_sku = ''

print("All 498 Product Name, Links, and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr, 
                  'Descripcion2': product_descr2,
                  'Foto': product_img,
                    'SKU': product_sku})

df.to_csv('helvex/excel_helvex.csv', index=False)

print("Spreadsheet with columns, 'Producto' and 'Descripcion' Successfully Written")
