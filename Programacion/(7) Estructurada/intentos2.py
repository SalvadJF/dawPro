import sys
intentos = 0

while True:
    intentos += 1
    if intentos > 3:
        print('Me canse.')
        sys.exit(1)
    try:
        x = int(input('Introduzca el primer numero: '))
        break
    except ValueError:
        print('El dato introducido no es un numero entero.')
intentos = 0
while True:
    intentos += 1
    if intentos > 3:
        print('Me canse')
        sys.exit(1)
    try:
        y = int('Introduzca el segundo numero: ')
        break
    except ValueError:
        print('El dato introducido no es un numero entero.')
print('El resultado es:', x + y)
