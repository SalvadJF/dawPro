"""Escribir un programa que calcule el máximo común divisor de dos números enteros
introducidos por teclado, usando:
a) La función math.gcd.
b) Bucles."""

#a)

from math import gcd

while True:
    try:
        a = int(input('Introduzca el primer numero: '))
        b = int(input('Introduzca el segundo numero: '))
        if 0 in (a, b):
            print('No puede haber ningun cero.')
        else:
            break
    except ValueError:
        print('El dato introducido no es correcto: ')

res = gcd(a , b)
print('El maximo comun divisor es', res)

#b

while True:
    try:
        a = int(input('Introduzca el primer numero: '))
        b = int(input('Introduzca el segundo numero: '))
        if 0 in (a, b):
            print('No puede haber ningun cero.')
        else:
            break
    except ValueError:
        print('El dato introducido no es correcto: ')
"""
def mcd(a, b):
    resto = a % b
    if resto == 0:
        return b
    return mcd (b, resto)
"""
def mcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

res2 = mcd(a, b)
print('El maximo comun divisor es', res2)
