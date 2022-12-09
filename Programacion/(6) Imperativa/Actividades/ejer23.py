"""Hacer el mismo ejercicio anterior, pero recogiendo el nombre del archivo desde la línea
de órdenes del sistema operativo. (Indicación: usar sys.argv)"""
import sys
if len(sys.argv) >= 2:
    nombre = sys.argv[1]
else:
    nombre = 'prueba.txt'

f = open(nombre, 'r')
while True:
    linea = f.readline().trip()
    if linea == '':
        break
    print(linea)
f.close()
