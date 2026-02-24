import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

productos = "https://helvex.com.mx/productos/bano"

response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('helvex/pages/page1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

for i in range(2,38):
    response = requests.get("https://helvex.com.mx/productos/bano?p=" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('helvex/pages/page' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "productos/" + str(i) + '/ HTML downloaded')

print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES