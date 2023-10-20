"""Escribir un programa que determine si un número entero introducido por teclado es
primo o compuesto."""

def es_primo(n):
    def divisores(n):
        res = 0
        i = 1
        while i <= n:
            if n % i == 0:
                res += 1
            i += 1
        return res
    return divisores(n) == 2

while True:
    try:
        num = int(input('Introduzca un numero entero: '))
        if num < 2 :
            print('Introduzca un numero mayor de 1')
        else:
            break
    except ValueError:
        print('El dato no introducido no es correcto')

if es_primo(num):
    print('EL numero', num, 'es primo')
else:
    print('El numero', num, 'NO es primo')
