import requests
from bs4 import BeautifulSoup
import re
import time

# START OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (154 PRODUCTS IN 18 PAGES)

product_links = []

for i in range(1,19):
    with open("tendenzza/pages/page" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'"slug":"([^"]+)","sap_id"', text)
    product_links.extend(match_link)
product_links = list(set(product_links))

# END OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (154 PRODUCTS IN 18 PAGES)

# START OF DOWNLOADING PRODUCT HTML FILES (154 FILES)

product_no = 1
for link in product_links:
    current = 'https://tendenzza.it/productos/1/' + link
    response = requests.get(current)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('tendenzza/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')

# END OF DOWNLOADING PRODUCT HTML FILES (154 FILES)


