"""
8 Unos verdaderos, ceros falsos
Crear una función que devuelva una lista de valores booleanos, a partir de un número dado.
Repitiendo el dígito del número uno a la vez, agregar True si el dígito es 1 y False si es 0.
"""
prueba = ("100101")

def boleano(a):
    return [bool(int(i)) for i in a]

boleano(prueba)

def prueba2(n):
    return [i == '1' for i in str(n)]
