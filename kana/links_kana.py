import requests
from bs4 import BeautifulSoup
import re
import time

# START OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (498 PRODUCTS IN 42 PAGES)

product_links = []

with open("kana/pages/page1" + ".txt", "r", encoding='utf-8') as file:
    text = file.read()
match_link = re.findall(
    r'href="(https:\/\/kana\.lat\/tienda\/[a-z]+\/.*?\/)"', text)
product_links.extend(match_link)
product_links = list(set(product_links))

# END OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (498 PRODUCTS IN 42 PAGES)

# START OF DOWNLOADING PRODUCT HTML FILES (498 FILES)

product_no = 1

for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('kana/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')

# END OF DOWNLOADING PRODUCT HTML FILES (498 FILES)


