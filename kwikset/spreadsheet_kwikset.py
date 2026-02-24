import re
import pandas as pd

i = 1

product_names = []
product_descr = []

while i < 17:
    with open("kwikset/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<h1 class="product_title entry-title">\s+(.+)\s+<\/h1>', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<div class="woocommerce-product-details__short-description">\s+<p>\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+.*\s+(.+)\s+', text)


    product_names.append(match_name)
    product_descr.append(match_desc)

    i += 1

    match_name = ''
    match_desc = ''

print("All 16 Product Names and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr
                  })

df.to_csv('kwikset/productos_kwikset.csv', index=False)

print("Spreadsheet with columns, 'Producto' and 'Descripcion' Successfully Written")
