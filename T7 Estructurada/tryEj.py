while True:

    try:
        x = int(input('Introduzca el primer numero: '))
        y = int(input('Introduzca el segundo numero: '))
        print('El resultado es:', x + y)
        break
    except ValueError:
        print('El dato introducido no es un numero entero.')
