"""
125. Dado el documento XML del ejercicio anterior, escribir un programa que elimine al
socio cuyo id sea 51 y guarde los cambios en el mismo archivo.
"""
import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')

raiz = arbol.getroot()

socio = raiz.find('./socios/socio[@id="51"]')
padre = raiz.find('./socios/socio[@id="51"]/..')
#raiz.find('socios') tambien seria valida
padre.remove(socio)

arbol.write('club.xml')
