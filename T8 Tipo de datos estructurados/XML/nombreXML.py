import xml.etree.ElementTree as ET
arbol = ET.parse('archivo.xml')
raiz = arbol.getroot()

for hijo in raiz:
    if hijo.tag == 'alumno':
        nombre = hijo[1]
        propio = nombre[0].text
        apellidos = nombre[1].text
        print(propio, apellidos)
