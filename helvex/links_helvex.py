import requests
from bs4 import BeautifulSoup
import re
import time

# START OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (621 PRODUCTS IN 52 PAGES)

product_links = []

for i in range(1,38):
    with open("helvex/pages/page" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<a class="product-item-link" href="(.+)">', text)
    product_links.extend(match_link)
product_links = list(set(product_links))

# END OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (621 PRODUCTS IN 52 PAGES)

# START OF DOWNLOADING PRODUCT HTML FILES (621 FILES)

product_no = 1

for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('helvex/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')

# END OF DOWNLOADING PRODUCT HTML FILES (621 FILES)


