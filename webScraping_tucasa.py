# -*- coding: utf-8 -*-
"""
Tipologia i cicle de vida de les dades
Pràctica 1
Narcís Coll Follia i Elisabet Ejarque Gonzalez
Abril de 2020

Projecte de web scraping del portal www.tucasa.com
per poder fer el seguiment dels preus dels pisos de lloguer
"""
import requests
from bs4 import BeautifulSoup
# import csv


# Bcn capital, pag 1
url = "https://www.tucasa.com/alquiler/viviendas/barcelona/?r=&idz=0008&ord=&pgn=1"
# Bcn província, pag 1
# url = "https://www.tucasa.com/alquiler/viviendas/barcelona/?r=&idz=0008&ord=&pgn=1"

# Càrrega de la pàgina web
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Càrrega d'un anunci
anunci = soup.find('div', class_='contenedor-descripcion-inmueble')
#print(anunci.prettify())

# %% 
# Càrrega dels atributs d'un anunci

print("preu")
# Agafem tot el contingut del tag
preu_str = anunci.find('div', class_='div-precio-cards hidden-listado').span.text.strip()
# Ens quedem només amb el valor
preu = preu_str.split(" ")[0]
print(preu)


print("m2")
m2_str = anunci.find('li', class_="metros-cuadrados").text
m2 = m2_str.split(" ")[0]
print(m2)
      

print("nHab")
nHab_str = anunci.find('li', class_="num-habitaciones hidden-xs hidden-sm").text
nHab = nHab_str.split(" ")[0]
print(nHab)


print("nBanys")
nBanys_str = anunci.find('li', class_="num-baños").text
nBanys = nBanys_str.split(" ")[0]
print(nBanys)


print("preu_m2")
preu_m2_str = anunci.find('li', class_="precio-metro hidden-cards hidden-xs").text
preu_m2 = preu_m2_str.split(" ")[0]
print(preu_m2)


print("zona")
zona = anunci.find('span', class_='titulo-inmueble').text.strip()
print(zona)


print("carrer")
carrer = anunci.find('span', class_='calle-inmueble').text.strip()
print(carrer)






