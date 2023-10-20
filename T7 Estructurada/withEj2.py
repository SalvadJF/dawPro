nombre= input('Introduzca el nombre del archivo: ')
if nombre == '':
    nombre = 'prueba.txt'

with open(nombre, 'r') as f:
    while True:
        try:
            linea = f.readline().strip()
            if linea == '':
                break
            print(linea)
        except FileNotFoundError:
            print('Archivo no encontrado.')
