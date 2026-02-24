import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

productos = "https://urrea.mx/banos/llaves-para-banos"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('urrea/pages/llaves1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2,7):
    response = requests.get("https://urrea.mx/banos/llaves-para-banos?page="+str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/pages/llaves' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "productos/" + str(i) + '/ HTML downloaded')

productos = "https://urrea.mx/banos/regaderas"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('urrea/pages/reg1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2,5):
    response = requests.get("https://urrea.mx/banos/regaderas?page="+str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/pages/reg' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "productos/" + str(i) + '/ HTML downloaded')

productos = "https://urrea.mx/banos/ceramicos"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('urrea/pages/cer1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2,6):
    response = requests.get("https://urrea.mx/banos/ceramicos?page="+str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/pages/cer' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "productos/" + str(i) + '/ HTML downloaded')

productos = "https://urrea.mx/banos/accesorios"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('urrea/pages/acc1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
for i in range(2,6):
    response = requests.get("https://urrea.mx/banos/accesorios?page="+str(i))
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/pages/acc' + str(i) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(productos + "productos/" + str(i) + '/ HTML downloaded')

productos = "https://urrea.mx/cocina/llaves-para-cocina"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('urrea/pages/cocina1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://urrea.mx/cocina/llaves-para-cocina?page=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('urrea/pages/cocina2.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())


# END OF DOWNLOADING PRODUCT-PAGES HTML FILES