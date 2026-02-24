# import requests
# from bs4 import BeautifulSoup
import pandas as pd
import re
import time


def count_occurrences(text, pattern):
    matches = re.findall(pattern,text)
    for match in matches:
        print(match)
    return len(re.findall(pattern, text))

"""
response = requests.get("https://www.daltile.com.mx/app/pdetalle//Royalwalnut/")
soup = BeautifulSoup(response.text, 'html.parser')
with open('royal.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())


with open('royal.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'<div class="mosaico_right">\s+<div>\s+<div>\s+(.*)\s+<\/div>'
pattern2 = r'<table class="detalle_productos">\s*<tr>\s*<td>\s*<label>\s*Formato\s*<\/label>\s*<div>\s*(.*)\s*<\/div>'
pattern3 = r'<td>\s+<label>\s+Uso\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>'
pattern4 = r'<td>\s+<label>\s+Espesor\sde\sboquilla\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>'
pattern5 = '<td>\s+<label>\s+Recomendaciones\sde\sboquilla\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>'
pattern6 = '<td>\s+<label>\s+Adhesivo\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>'

"""


i = 1

product_names = []
product_desc1 = []
product_desc2 = []
product_desc3 = []
product_desc4 = []
product_desc5 = []
product_desc6 = []

while i < 252:
    with open("daltile/products/product" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_name = re.findall(
        r'<div class="mosaico_right">\s+<div>\s+<div>\s+(.*)\s+<\/div>', text)  # Regular Expression (Regex)
    match_desc1 = re.findall(
        r'<table class="detalle_productos">\s*<tr>\s*<td>\s*<label>\s*Formato\s*<\/label>\s*<div>\s*(.*)\s*<\/div>', text)  # Regular Expression (Regex)
    match_desc2 = re.findall(
        r'<td>\s+<label>\s+Uso\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>', text)
    match_desc3 = re.findall(
        r'<td>\s+<label>\s+Espesor\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>', text)
    match_desc4 = re.findall(
        r'<td>\s+<label>\s+Espesor\sde\sboquilla\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>', text)
    match_desc5 = re.findall(
        r'<td>\s+<label>\s+Recomendaciones\sde\sboquilla\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>', text)
    match_desc6 = re.findall(
        r'<td>\s+<label>\s+Adhesivo\s+<\/label>\s+<div>\s+(.*)\s+<\/div>\s+<\/td>', text)

    product_names.extend(match_name)
    product_desc1.extend(match_desc1)
    product_desc2.extend(match_desc2)
    product_desc3.extend(match_desc3)
    product_desc4.extend(match_desc4)
    product_desc5.extend(match_desc5)
    product_desc6.extend(match_desc6)

    i += 1

    match_name = ''
    match_desc1 = ''
    match_desc2 = ''
    match_desc3 = ''
    match_desc4 = ''
    match_desc5 = ''
    match_desc6 = ''

print("All 251 Product Names and Descriptions Successfully Extracted")
print("Commencing Spreadsheet Build\n")


df = pd.DataFrame({'Producto': product_names,
                   'Color': product_desc1,
                   'Uso': product_desc2,
                   'Espesor': product_desc3,
                   'Espesor de boquilla': product_desc4,
                   'Recomendaciones de boquilla': product_desc5,
                   'Adhesivo': product_desc6
                   })

df.to_csv('daltile/productos.csv', index=False)

print("Spreadsheet with columns, 'Producto' and 'Descripcion'Successfully Written")
