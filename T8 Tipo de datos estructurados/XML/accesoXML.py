#Para leer un documento XML

import xml.etree.ElementTree as ET
arbol = ET.parse('archivo.xml')
raiz = arbol.getroot()

#Como recorrer el documento XML desde la raiz

for hijo in raiz:
    print(hijo.tag, hijo.attrib)

"""
Ejemplo de filtrar

for hijo in raiz:
    if hijo.tag == 'alummno'and 'matricula in hijo.attrib:
        print(hijo.attrib['matricula'])

"""
#Tambien se puede accder por indexacion

raiz[0]
raiz[1]
raiz[3]

"""para acceder a cuantos hijos hay podemos usar len(raiz)"""

#para acceder a datos dentro del hijo se puede usar indexacion

raiz[0][0]

#si ya es el fin usamos text para sacar su contenido

raiz[0][0].text
