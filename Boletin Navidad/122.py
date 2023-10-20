"""
122. Dado el documento XML del ejercicio anterior, escribir un programa que cuente cuántos
socios tiene el club y lo muestre por pantalla.
"""
import xml.etree.ElementTree as ET

arbol = ET.parse('club.xml')

raiz = arbol.getroot()

len(raiz.findall('./socios/socio'))
