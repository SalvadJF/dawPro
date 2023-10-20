#mover informacion en XML
import xml.etree.ElementTree as ET

arbol = ET.parse('archivo.xml')

raiz = arbol.getroot()

#combinamos append o insert con remove para ello

madre = raiz.find('madre')
raiz.remove(madre)
alumno = raiz.find('alumno')
alumno.append(madre)
