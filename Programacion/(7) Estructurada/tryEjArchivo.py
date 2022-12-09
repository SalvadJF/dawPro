try:
    f = open('entrada.txt', 'r')
    lineas = f.readlines()
    f.close()
    x, y = [int(x.strip()) for x in lineas]
    suma = x + y
    f = open('salida.txt', 'w')
    f.write(str(suma) + '\n')
    f.close()
    print('La operacion se ha realizado correctamente')
except FileNotFoundError:
    print('Archivo no encontrado.')
except ValueError:
    print('Las lineas del archivo deben contener un numero entero')
