import requests
from bs4 import BeautifulSoup
import re
import time

# START OF EXTRACTING UNIQUE PRODUCT LINKS FROM PRODUCT-PAGES (154 PRODUCTS IN 27 PAGES)

# product_links = []
# for i in range(1,4):
#     with open("llanodelatorre/pages/pisos" + str(i) + ".txt", "r", encoding='utf-8') as file:
#         text = file.read()
#     match_link = re.findall(
#         r'"linkText":"([^"]+)","brand"', text)
#     product_links.extend(match_link)
# product_links = list(set(product_links))
# product_no = 1
# for link in product_links:
#     current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
#     response = requests.get(current)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     with open('llanodelatorre/products/pisos' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
#         file.write(soup.prettify())
#     product_no += 1
#     print(link + 'HTML downloaded')


# product_links = []
# for i in range(1,5):
#     with open("llanodelatorre/pages/adhesivos" + str(i) + ".txt", "r", encoding='utf-8') as file:
#         text = file.read()
#     match_link = re.findall(
#         r'"linkText":"([^"]+)","brand"', text)
#     product_links.extend(match_link)
# product_links = list(set(product_links))
# product_no = 1
# for link in product_links:
#     current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
#     response = requests.get(current)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     with open('llanodelatorre/products/adhesivos' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
#         file.write(soup.prettify())
#     product_no += 1
#     print(link + 'HTML downloaded')


# product_links = []
# for i in range(1,5):
#     with open("llanodelatorre/pages/adhesivos" + str(i) + ".txt", "r", encoding='utf-8') as file:
#         text = file.read()
#     match_link = re.findall(
#         r'"linkText":"([^"]+)","brand"', text)
#     product_links.extend(match_link)
# product_links = list(set(product_links))
# product_no = 1
# for link in product_links:
#     current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
#     response = requests.get(current)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     with open('llanodelatorre/products/adhesivos' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
#         file.write(soup.prettify())
#     product_no += 1
#     print(link + 'HTML downloaded')


# product_links = []
# for i in range(1,13):
#     with open("llanodelatorre/pages/acc" + str(i) + ".txt", "r", encoding='utf-8') as file:
#         text = file.read()
#     match_link = re.findall(
#         r'"linkText":"([^"]+)","brand"', text)
#     product_links.extend(match_link)
# product_links = list(set(product_links))
# product_no = 1
# for link in product_links:
#     current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
#     response = requests.get(current)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     with open('llanodelatorre/products/accesorios' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
#         file.write(soup.prettify())
#     product_no += 1
#     print(link + 'HTML downloaded')


# product_links = []
# for i in range(1,3):
#     with open("llanodelatorre/pages/cocina" + str(i) + ".txt", "r", encoding='utf-8') as file:
#         text = file.read()
#     match_link = re.findall(
#         r'"linkText":"([^"]+)","brand"', text)
#     product_links.extend(match_link)
# product_links = list(set(product_links))
# product_no = 1
# for link in product_links:
#     current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
#     response = requests.get(current)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     with open('llanodelatorre/products/cocina' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
#         file.write(soup.prettify())
#     product_no += 1
#     print(link + 'HTML downloaded')


product_links = []
for i in range(1,4):
    with open("llanodelatorre/pages/muebles" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'"linkText":"([^"]+)","brand"', text)
    product_links.extend(match_link)
product_links = list(set(product_links))
product_no = 1
for link in product_links:
    current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
    response = requests.get(current)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('llanodelatorre/products/muebles' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')


# product_links = []
# for i in range(1,4):
#     with open("llanodelatorre/pages/cal" + str(i) + ".txt", "r", encoding='utf-8') as file:
#         text = file.read()
#     match_link = re.findall(
#         r'"linkText":"([^"]+)","brand"', text)
#     product_links.extend(match_link)
# product_links = list(set(product_links))
# product_no = 1
# for link in product_links:
#     current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
#     response = requests.get(current)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     with open('llanodelatorre/products/calentadores' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
#         file.write(soup.prettify())
#     product_no += 1
#     print(link + 'HTML downloaded')


# product_links = []
# for i in range(1,4):
#     with open("llanodelatorre/pages/otros" + str(i) + ".txt", "r", encoding='utf-8') as file:
#         text = file.read()
#     match_link = re.findall(
#         r'"linkText":"([^"]+)","brand"', text)
#     product_links.extend(match_link)
# product_links = list(set(product_links))
# product_no = 1
# for link in product_links:
#     current = 'https://www.llanodelatorre.com.mx/' + link + '/p'
#     response = requests.get(current)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     with open('llanodelatorre/products/otros' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
#         file.write(soup.prettify())
#     product_no += 1
#     print(link + 'HTML downloaded')

