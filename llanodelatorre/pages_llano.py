import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

productos = "https://www.llanodelatorre.com.mx/pisos-y-muros/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/pisos1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2, 4):
    response = requests.get("https://www.llanodelatorre.com.mx/pisos-y-muros/?page=" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('llanodelatorre/pages/pisos' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "page/" + str(i) + '/ HTML downloaded')

productos = "https://www.llanodelatorre.com.mx/adhesivo/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/adhesivos1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2, 5):
    response = requests.get("https://www.llanodelatorre.com.mx/adhesivo/?page=" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('llanodelatorre/pages/adhesivos' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "page/" + str(i) + '/ HTML downloaded')

productos = "https://www.llanodelatorre.com.mx/accesorios-para-bano/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/acc1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2, 13):
    response = requests.get("https://www.llanodelatorre.com.mx/accesorios-para-bano/?page=" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('llanodelatorre/pages/acc' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "page/" + str(i) + '/ HTML downloaded')

productos = "https://www.llanodelatorre.com.mx/accesorios-para-cocina/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/cocina1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2, 3):
    response = requests.get("https://www.llanodelatorre.com.mx/accesorios-para-cocina/?page=" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('llanodelatorre/pages/cocina' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "page/" + str(i) + '/ HTML downloaded')

productos = "https://www.llanodelatorre.com.mx/sanitarios-y-muebles-para-bano/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/muebles1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2, 4):
    response = requests.get("https://www.llanodelatorre.com.mx/sanitarios-y-muebles-para-bano/?page=" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('llanodelatorre/pages/muebles' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "page/" + str(i) + '/ HTML downloaded')

productos = "https://www.llanodelatorre.com.mx/calentadores-y-tinacos/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/cal1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2, 4):
    response = requests.get("https://www.llanodelatorre.com.mx/calentadores-y-tinacos/?page=" + str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('llanodelatorre/pages/cal' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "page/" + str(i) + '/ HTML downloaded')

productos = "https://www.llanodelatorre.com.mx/complementos-y-otros/"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/otros1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.llanodelatorre.com.mx/complementos-y-otros/?page=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('llanodelatorre/pages/otros2.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

















print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES