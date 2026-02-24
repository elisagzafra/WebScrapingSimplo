import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

productos = "https://kana.lat/tienda/"

response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('kana/pages/page1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES