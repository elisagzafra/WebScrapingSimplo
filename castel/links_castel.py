import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

productos = "https://castel.com.mx/productos/"

response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('castel/pages/page1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

for i in range(2, 43):
    response = requests.get("https://castel.com.mx/productos/page/" + str(i) +'/')
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('castel/pages/page' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "page/" + str(i) + '/ HTML downloaded')

print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES

# START OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (498 PRODUCTS IN 42 PAGES)

product_links = []

for i in range(1, 43):
    with open("castel/pages/page" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<a class="woocommerce-LoopProduct-link" href="(.+)">', text)
    product_links.extend(match_link)

product_links = list(set(product_links))

# END OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (498 PRODUCTS IN 42 PAGES)

# START OF DOWNLOADING PRODUCT HTML FILES (498 FILES)

product_no = 1

for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('castel/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')

# END OF DOWNLOADING PRODUCT HTML FILES (498 FILES)


