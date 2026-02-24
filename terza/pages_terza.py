import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

alfombras = "https://www.terza.com/alfombras/catalogo"
response = requests.get(alfombras)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

pasto = "https://www.terza.com/pasto-sintetico/catalogo"
response = requests.get(pasto)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page2.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

persianas = "https://www.terza.com/persianas/catalogo"
response = requests.get(persianas)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page3.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

muros = "https://www.terza.com/muros-verdes/catalogo"
response = requests.get(muros)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page4.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

madera = "https://www.terza.com/pisos-de-madera/catalogo"
response = requests.get(madera)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page5.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

laminados = "https://www.terza.com/pisos-laminados/catalogo"
response = requests.get(laminados)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page6.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

vinilicos = "https://www.terza.com/piso-vinilico/catalogo"
response = requests.get(vinilicos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page7.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

deck = "https://www.terza.com/pisos-deck/catalogo"
response = requests.get(deck)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page8.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

tapetes = "https://www.terza.com/tapetes/catalogo"
response = requests.get(tapetes)
soup = BeautifulSoup(response.text, 'html.parser')
with open('terza/pages/page9.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())


print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES