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

# Inicialitzem el número de pàgina
num_pag = 1


# Loop sobre les diferents pàgines de la cerca (de moment només 2 per no haver de treure masses resultats per pantalla)
for i in range(2):
    # Bcn província, pag 1
    url = "https://www.tucasa.com/alquiler/viviendas/barcelona/?r=&idz=0008&ord=&pgn=" + str(num_pag)


    # Càrrega de la pàgina web
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Loop sobre tots els anuncis d'una pàgina
    for anunci in soup.find_all('div', class_='contenedor-descripcion-inmueble'):
        #print(anunci.prettify())

        # %% 
        # Càrrega dels atributs d'un anunci

        print("preu")
        # Per cada atribut utilitzem try ja que hi ha casos especials que no tenen totes les etiquetes que busquem
        try:
            # Agafem tot el contingut del tag
            preu_str = anunci.find('div', class_='div-precio-cards hidden-listado').span.text.strip()
            # Ens quedem només amb el valor
            preu = preu_str.split(" ")[0]
        except Exception as e:
            preu = None
        print(preu)


        print("m2")
        try:
            m2_str = anunci.find('li', class_="metros-cuadrados").text
            m2 = m2_str.split(" ")[0]
        except Exception as e:
            m2 = None   
        print(m2)
        

        print("nHab") 
        try:
            nHab_str = anunci.find('li', class_="num-habitaciones hidden-xs hidden-sm").text
            nHab = nHab_str.split(" ")[0]
        except Exception as e:
            nHab = None  
        print(nHab)

        
        print("nBanys")
        try:
            nBanys_str = anunci.find('li', class_="num-baños").text
            nBanys = nBanys_str.split(" ")[0]
        except Exception as e:
            nBanys = None
        print(nBanys)


        print("preu_m2")
        try:
            preu_m2_str = anunci.find('li', class_="precio-metro hidden-cards hidden-xs").text
            preu_m2 = preu_m2_str.split(" ")[0]
        except Exception as e:
            preu_m2 = None
        print(preu_m2)


        print("zona")
        try:
            zona = anunci.find('span', class_='titulo-inmueble').text.strip()
        except Exception as e:
            zona = None
        print(zona)


        print("carrer")
        try:
            carrer = anunci.find('span', class_='calle-inmueble').text.strip()
        except Exception as e:
            carrer = None
        print(carrer)

        print()

    #Incrementem el número de pàgina
    num_pag = num_pag + 1





