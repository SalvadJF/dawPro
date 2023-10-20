#Escribir en un archivo xml

import xml.etree.ElementTree as ET

arbol = ET.parse('archivo.xml')

raiz = arbol.getroot()

for nota in raiz.iter('nota'):
    nueva_nota = int(nota.text) + 1
    nota.text = str(nueva_nota)
    nota.set('modificado', 'si')

arbol.write('salida.xml')
#Esto crea un nuevo archivo XML con los datos nuevos
