"""
4 Cantidad total de caracteres únicos
Dadas dos cadenas, crear una función que
devuelva el número total de caracteres únicos de la cadena combinada.

"""

a = 'hola'
b = 'un'
c = 'perro'
d = 'gato'

def unicos(a, b):
    return print(len(set(a + b)))

unicos(a, b)
unicos(c, d)
