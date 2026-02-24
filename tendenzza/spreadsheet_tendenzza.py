import re
import pandas as pd

i = 1

product_names = []
product_descr = []

while i < 155:
    with open("tendenzza/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<h1 class="ff-helvetica-neue-co tx-28 xl:tx-34 xxl:tx-42 tx-normal mb-4">\s*(.+)\s*<\/h1>', text) # Regular Expression (Regex)
    match_desc = re.findall(
        r'<p class="ff-roboto tx-12 tx-darkgrey-1 line-h-soft">\s*(.+)\s*<\/p>', text)

    product_names.append(match_name)
    product_descr.append(match_desc)

    i += 1

    match_name = ''
    match_desc = ''

print("All 154 Product Names and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                  'Descripcion': product_descr, 
                  })

df.to_csv('tendenzza/excel_tendenzza.csv', index=False)

print("Spreadsheet with columns, 'Producto' and 'Descripcion' Successfully Written")
