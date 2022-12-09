nombre= input('Introduzca el nombre del archivo: ')
if nombre == '':
    nombre = 'prueba.txt'

f = open(nombre, 'r')
while True:
    try:
        linea = f.readline().strip()
        if linea == '':
            break
        print(linea)
    except FileNotFoundError:
        print('Archivo no encontrado.')
    f.close()
