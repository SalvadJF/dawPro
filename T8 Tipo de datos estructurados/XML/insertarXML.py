#insertar nueva informacion en un XML
import xml.etree.ElementTree as ET

arbol = ET.parse('archivo.xml')

raiz = arbol.getroot()

telefono = ET.Element('telefono')
telefono.text = '956366666'
madre = raiz.find('madre')
madre.append(telefono)
#tambien podriamos haber usado el insert
#y colocar el telefono el primero, asignado su posicion
#madre.insert(0, telefono)

#La función SubElement también proporciona una forma muy conveniente de crear sub-elementos

a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)
#Resultado <a><b /><c><d /></c></a>
