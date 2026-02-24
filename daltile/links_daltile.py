import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

productos = "https://www.daltile.com.mx/app/productos"

response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('daltile/pages/page0.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

for i in range(13,260,13):
    response = requests.get("https://www.daltile.com.mx/app/productos/" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('daltile/pages/page' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "productos/" + str(i) + '/ HTML downloaded')

print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES

# START OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (251 PRODUCTS IN 20 PAGES)

product_links = []

for i in range(0,260,13):
    with open("daltile/pages/page" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'href="(https:\/\/www\.daltile\.com\.mx\/app\/pdetalle\/.*?)"', text)
    product_links.extend(match_link)
product_links = list(set(product_links))

# END OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (251 PRODUCTS IN 20 PAGES)

# START OF DOWNLOADING PRODUCT HTML FILES (251 FILES)

product_no = 1

for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('daltile/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')

# END OF DOWNLOADING PRODUCT HTML FILES (251 FILES)


