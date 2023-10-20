import sys

intentos = 0
while True:
    intentos += 1
    if intentos > 3:
        print('Me canse.')
        sys.exit(1)
    try:
        x = int(input('Introduzca el primer numero: '))
        y = int(input('Introduzca el segundo numero: '))
        print('El resultado es:', x + y)
        break
    except ValueError:
        print('El dato introducido no es un numero entero.')
