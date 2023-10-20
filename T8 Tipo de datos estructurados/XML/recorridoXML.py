import xml.etree.ElementTree as ET
arbol = ET.parse('archivo.xml')
raiz = arbol.getroot()

#Recorre todos los nodos desde el que eliga en profundidad
for nodo in raiz.iter():
    print(nodo.tag)

#Si se le pasa una etiqueta como argumento, devolverá únicamente los nodos que tengan esa etiqueta

for dni in raiz.iter('dni'):
    print(dni.text)
