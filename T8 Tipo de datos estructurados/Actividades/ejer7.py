"""
7 Purgar y organizar
Dada una lista de números, escribir una función que devuelva una lista que. . .
1. Elimine todos los elementos duplicados.
2. Esté ordenado de menor a mayor valor"""

a = (1, 1, 100, 2, 3, 4, 4, 5, 6,)

def purga(a):
    return sorted(set(a))

print(purga(a))
