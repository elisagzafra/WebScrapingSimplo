import requests
from bs4 import BeautifulSoup
import re
import time

# START OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (347 PRODUCTS IN 8 PAGES)

product_links = []

for i in range(1,348):
    with open("terza/pages/page" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<a href="(.+)" class="product_cat">', text)
    product_links.extend(match_link)
product_links = list(set(product_links))

# END OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (347 PRODUCTS IN 8 PAGES)

# START OF DOWNLOADING PRODUCT HTML FILES (347 FILES)

product_no = 1

for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('terza/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')

# END OF DOWNLOADING PRODUCT HTML FILES (347 FILES)


