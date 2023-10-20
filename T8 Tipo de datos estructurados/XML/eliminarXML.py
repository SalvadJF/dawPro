#Eliminar un elemento del XML
import xml.etree.ElementTree as ET

arbol = ET.parse('archivo.xml')

raiz = arbol.getroot()

for alumno in raiz.findall('alumno'):
    # se usa findall para que no afecte el borrado durante el recorrido
    nota = int(alumno.find('nota').text)
    if nota < 9:
        raiz.remove(alumno)
#Crea un nuevo XML con el elemento borrado
arbol.write('salida.xml')
