"""
124. Dado el documento XML del ejercicio anterior, escribir un programa que cambie la
dirección del socio cuyo id sea 1 por «Calle Ancha, 35» y guarde los cambios en el
mismo archivo.
"""
import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')

raiz = arbol.getroot()

#Esto localiza el socio con esa id a culaquier nivel de la raiz
socio = raiz.find('.//socio[@id="1"]')
direccion = socio.find('direccion')
direccion.text = 'Calle Ancha, 35'

arbol.write('club.xml')
