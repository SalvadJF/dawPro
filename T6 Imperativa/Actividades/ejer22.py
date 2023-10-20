"""Escribir un programa que solicite al usuario el nombre de un archivo de texto y muestre
su contenido en pantalla. Si no se proporciona ningún nombre de archivo, el programa
usará por defecto prueba.txt."""

nombre= input('Introduzca el nombre del archivo: ')
if nombre == '':
    nombre = 'prueba.txt'

f = open(nombre, 'r')
while True:
    linea = f.readline().strip()
    if linea == '':
        break
    print(linea)
f.close()
