"""
5 ¿Cuál es tu tipo?
Python tiene tres tipos principales de estructuras de datos formadas por objetos más pequeños:
• Listas, escritas con corchetes [], como [1, 2, 4, 8].
• Tuplas, escritas entre paréntesis (), como (7, 8, 9).
• Conjuntos, escritos con llaves {}, como {2, 3, 5, 7, 11, 13}.
Cada uno de estos tipos tiene sus propias propiedades y peculiaridades especiales que vale la
pena conocer, pero este ejercicio solo consiste en transformar estos tipos de datos entre sí.
Esto se puede hacer de la siguiente manera:
• tuple([1, 2, 4, 8]) devuelve (1, 2, 4, 8)
• list({2, 3, 5, 7, 11}) devuelve [2, 3, 5, 7, 11, 13]
• set((1, 2, 4)) devuelve {1, 2, 4}
Dadas dos estructuras de datos, data1 y data2, devolver data2 convertido al tipo de data1."""
t = (1, 2, 4, 8)
l = [2, 3, 5, 7, 11, 13]
s = {1, 2, 4}

def convertir(a, b):
    return print(type(a)(b))

convertir(t, l)
convertir(l, s)
convertir(s, t)
