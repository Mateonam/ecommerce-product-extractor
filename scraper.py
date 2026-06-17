import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'http://books.toscrape.com/'
respuesta = requests.get(url)
datos_extraidos = []
sopa = BeautifulSoup(respuesta.text, 'html.parser')

libros = sopa.find_all('article', class_='product_pod')

for libro in libros:
    titulo = libro.h3.a['title']
    precio = libro.find('p', class_='price_color').text.replace('Â', '')
    datos_extraidos.append({'Título': titulo, 'Precio': precio})

for dato in datos_extraidos[:5]:
    print(dato)

df = pd.DataFrame(datos_extraidos)
df.to_excel('Libros_extraidos.xlsx', index=False)

print("Archivo de excel creado con éxito")