import re
import pandas as pd

i = 1

product_names = []
product_descr = []
product_links = []

while i <73:
    with open("llanodelatorre/products/otros" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<span class="vtex-store-components-3-x-productBrand vtex-store-components-3-x-productBrand--quickview">\s*(.+)\s*<!-- -->', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<div style="display:contents">\s*(.+)\s*<\/div>', text)
    match_links = re.findall(
        r'<link data-react-helmet="true" href="(.+)" rel="canonical"\/>', text)

    product_names.append(match_name)
    product_descr.append(match_desc)
    product_links.append(match_links)

    i += 1

    match_name = ''
    match_desc = ''
    match_links = ''

df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr,
                  'Link': product_links
                  })

df.to_csv('llanodelatorre/spreadsheets/otros_llano.csv', index=False)

print("Spreadsheet with columns, 'Producto', 'Link' and 'Descripcion' Successfully Written")
