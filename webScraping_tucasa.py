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
import csv
csv_file = open('webScraping_tucasa.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ciutat', 'pagina', 'zona', 'carrer', 'preu', 'm2', 'preu_m2', 'nHab', 'nBanys'])

# Ciutats que volem escrapejar: Diccionari amb les url inicials
ciutats = {"girona": "https://www.tucasa.com/alquiler/viviendas/girona/girona-capital/?r=&idz=0017.0001.9999.0001&ord=&pgn=1", 
           "tarragona": "https://www.tucasa.com/alquiler/viviendas/tarragona/tarragona-capital/?r=&idz=0043.0001.9999.0001&ord=&pgn=1", 
           "lleida": "https://www.tucasa.com/alquiler/viviendas/lleida/lleida-capital/?r=&idz=0025.0001.9999.0001&ord=&pgn=1",
           "barcelona": "https://www.tucasa.com/alquiler/viviendas/barcelona/barcelona-capital/?r=&idz=0008.0001.9999.0001&ord=&pgn=1"}

# Loop sobre cada ciutat
for ciutat in ciutats:
    
    url = ciutats[ciutat]

    # Loop sobre les diferents pàgines de la cerca
    while url != None:
            
        # Càrrega de la pàgina web
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
    
        # Loop sobre tots els anuncis d'una pàgina
        for anunci in soup.find_all('div', class_='contenedor-descripcion-inmueble'):
                
            # Càrrega dels atributs de cada anunci
    
            # Per cada atribut utilitzem try ja que hi ha casos especials que no tenen totes les etiquetes que busquem
            try:
                # Agafem tot el contingut del tag
                preu_str = anunci.find('div', class_='div-precio-cards hidden-listado').span.text.strip()
                # Ens quedem només amb el valor
                preu = preu_str.split(" ")[0]
            except Exception as e:
                preu = None
    
            try:
                m2_str = anunci.find('li', class_="metros-cuadrados").text
                m2 = m2_str.split(" ")[0]
            except Exception as e:
                m2 = None   
            
            try:
                nHab_str = anunci.find('li', class_="num-habitaciones hidden-xs hidden-sm").text
                nHab = nHab_str.split(" ")[0]
            except Exception as e:
                nHab = None  
            
            try:
                nBanys_str = anunci.find('li', class_="num-baños").text
                nBanys = nBanys_str.split(" ")[0]
            except Exception as e:
                nBanys = None
            
            try:
                preu_m2_str = anunci.find('li', class_="precio-metro hidden-cards hidden-xs").text
                preu_m2 = preu_m2_str.split(" ")[0]
            except Exception as e:
                preu_m2 = None
            
            try:
                zona = anunci.find('span', class_='titulo-inmueble').text.strip()
            except Exception as e:
                zona = None
            
            try:
                carrer = anunci.find('span', class_='calle-inmueble').text.strip()
            except Exception as e:
                carrer = None
            
            pagina = url.split("=")[-1]
            
            csv_writer.writerow([ciutat, pagina, zona, carrer, preu, m2, preu_m2, nHab, nBanys])
            
                
        # Url de la pàgina següent
        try:
            url0 = soup.find('div', class_="contenedor-paginacion-listado")
            url = url0.find_all('a', class_='btn-paginacion br5 tr05')[1]['href']
    
        except Exception as e:
            url = None

csv_file.close()




