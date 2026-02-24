import requests
from bs4 import BeautifulSoup
import re
import time

product_links = []
for i in range(1,6):
    with open("urrea/pages/acc" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<div class="piece">\s*<a href="(.+)">', text)
    product_links.extend(match_link)
product_links = list(set(product_links))
product_no = 1
for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')


product_links = []
for i in range(1,6):
    with open("urrea/pages/cer" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<div class="piece">\s*<a href="(.+)">', text)
    product_links.extend(match_link)
product_links = list(set(product_links))
product_no = 121
for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')


product_links = []
for i in range(1,3):
    with open("urrea/pages/cocina" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<div class="piece">\s*<a href="(.+)">', text)
    product_links.extend(match_link)
product_links = list(set(product_links))
product_no = 234
for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')


product_links = []
for i in range(1,7):
    with open("urrea/pages/llaves" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<div class="piece">\s*<a href="(.+)">', text)
    product_links.extend(match_link)
product_links = list(set(product_links))
product_no = 275
for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')


product_links = []
for i in range(1,5):
    with open("urrea/pages/reg" + str(i) + ".txt", "r", encoding='utf-8') as file:
        text = file.read()
    match_link = re.findall(
        r'<div class="piece">\s*<a href="(.+)">', text)
    product_links.extend(match_link)
product_links = list(set(product_links))
product_no = 408
for link in product_links:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open('urrea/products/product' + str(product_no) + '.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    product_no += 1
    print(link + 'HTML downloaded')


