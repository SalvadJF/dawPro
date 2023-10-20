import xml.etree.ElementTree as ET
arbol = ET.parse('archivo.xml')
raiz = arbol.getroot()

"""
El método findall devuelve una lista con los nodos que tengan una cierta etiqueta
y que sean hijos directos del nodo sobre el que se invoca.
"""
"""
El método find devuelve el primer hijo directo del nodo sobre el que se invoca,
siempre que tenga una cierta etiqueta indicada como argumento.
"""
"""
El método get devuelve el valor de algún atributo de la etiqueta asociada a ese nodo
"""
for alumno in raiz.findall('alumno'):
    numero = alumno.get('numero')
    dni = alumno.find('dni').text
    print(numero, dni)
