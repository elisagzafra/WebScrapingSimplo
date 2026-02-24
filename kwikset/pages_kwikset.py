import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

productos = "https://kwiksetlatam.com/cerrojos/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('kwikset/pages/cerrojos.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

productos = "https://kwiksetlatam.com/pomos/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('kwikset/pages/pomos.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

productos = "https://kwiksetlatam.com/gatillos/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('kwikset/pages/gatillos.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

productos = "https://kwiksetlatam.com/manijas/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('kwikset/pages/manijas.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

productos = "https://kwiksetlatam.com/electronicas/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('kwikset/pages/electronicas.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

productos = "https://kwiksetlatam.com/candados/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('kwikset/pages/candados.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())



print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES