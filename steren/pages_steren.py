import requests
from bs4 import BeautifulSoup
import re
import time

# START OF DOWNLOADING PRODUCT-PAGES HTML FILES

#SMART HOME
productos = "https://www.steren.com.mx/smart-home/focos-inteligentes"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page1.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/apagadores-inteligentes"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page2.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/contactos-inteligentes"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page3.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/camaras-de-seguridad-wifi"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page4.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/sistemas-de-seguridad-inteligente"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page5.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/casa-y-oficina-smart"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page6.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/repetidores-y-routers-wifi"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page7.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/asistentes-de-voz"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page8.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/smart-home/combos-smart-home-alexa"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page9.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
#TV Y VIDEO
productos = "https://www.steren.com.mx/tv-y-video/soportes-para-pantalla"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page10.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/cables-hdmi-y-de-video"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page11.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/antenas-para-tv"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page12.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/proyectores"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page13.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/sintonizadores-de-tv"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page14.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/controles-remoto-de-tv"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page15.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/accesorios-hdmi"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page16.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/amplificadores-y-selectores-de-video"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page17.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/adaptadores-y-convertidores-de-video"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page18.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/extensores-de-video"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page19.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/capturadoras-de-video"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page20.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/cables-vga"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page21.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/conectores-de-video"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page22.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/conectores-de-video?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page23.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/reguladores-de-voltaje-y-no-breaks"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page24.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/pico-digital"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page25.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/pico-digital?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page26.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/pico-digital?p=3"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page27.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/pico-digital?p=4"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page28.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/pico-digital?p=5"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page29.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/cables-coaxiales-por-metro"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page30.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/accesorios-de-tv-y-video-para-negocios"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page31.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/accesorios-de-tv-y-video-para-negocios?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page32.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/tv-y-video/gamers"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page33.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
#AUDIO
productos = "https://www.steren.com.mx/audio/audifonos"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page34.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/audifonos?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page35.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/bocinas"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page36.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/bafles-con-amplificador"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page37.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/microfonos"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page38.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/microfonos?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page39.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/luces-para-fiesta"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page40.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/receptores-de-audio-inalambrico"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page41.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/transmisores-fm"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page42.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/cables-de-audio"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page43.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/cables-de-audio?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page44.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/grabadoras-de-voz"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page45.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/megafonos"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page46.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/amplificadores-de-audio"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page47.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/bocinas-y-trompetas-pasivas"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page48.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/adaptadores-de-audio"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page49.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/adaptadores-de-audio?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page50.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/conectores-de-audio"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page51.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/audio/cables-de-audio-por-metro"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page52.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
#CABLES
productos = "https://www.steren.com.mx/cables/cables-para-celular-y-tablet"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page53.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-para-celular-y-tablet?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page54.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-de-audio"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page55.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-de-audio?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page56.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-hdmi-y-de-video"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page57.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-usb"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page58.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-usb?p=2"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page59.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-telefonicos"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page60.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-de-red"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page61.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/extensiones-electricas"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page62.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-de-alimentacion-interlock"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page63.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-vga"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page64.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/canaletas"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page65.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/organizadores-de-cables"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page66.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/grapas"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page67.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-y-accesorios-para-cctv"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page68.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-de-audio-por-metro"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page69.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-de-red-por-metro"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page70.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-telefonicos-por-metro"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page71.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-coaxiales-por-metro"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page72.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/cables/cables-multiconductor-por-metro"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page73.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
#SEGURIDAD
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/radios-intercomunicador-profesional"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page74.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/cajas-de-seguridad-cajas-fuerte"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page75.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/video-porteros-e-intercomunicadores"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page76.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/contadoras-y-detectores-de-billetes"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page77.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/camaras-cctv"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page78.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/grabadores-cctv-dvr"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page79.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/cables-y-accesorios-para-cctv"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page80.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/alarmas-y-sirenas"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page81.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
productos = "https://www.steren.com.mx/videovigilancia-y-seguridad/control-de-entrada"
response = requests.get(productos)
soup = BeautifulSoup(response.text, 'html.parser')
with open('steren/pages/page82.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

print("/n all page HTMLS downloaded")
time.sleep(3)

# END OF DOWNLOADING PRODUCT-PAGES HTML FILES