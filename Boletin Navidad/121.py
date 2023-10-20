"""
121. Dado un documento XML similar a éste (es decir, con la misma estructura pero no
necesariamente con el mismo contenido) y almacenado en el archivo club.xml:

escribir un programa que muestre los socios del club de forma similar a la siguiente:
[1] Sherlock Holmes
[51] Winston Churchill
"""
import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')

raiz = arbol.getroot()

for socio in raiz.findall('./socios/socio'):
    ident = socio.get('id')
    nombre = socio.find('nombre').text
    print(f'[{ident}] {nombre}')
