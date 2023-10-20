"""
127. Dado el documento XML del ejercicio anterior, escribir un programa que muestre el
nombre de los socios por orden cronológico según su fecha de alta, de más antiguo a
más reciente.
"""
import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')

raiz = arbol.getroot()

lst = []

for socio in raiz.iter('socio'):
    nombre = socio.find('nombre').text
    alta = socio.find('alta').text
    lst.append((alta, nombre))
lst.sort()
# usar la _ es la variable anonima, la cual no se usa
for _, nombre in lst:
    print(nombre)
