"""
Escribir en Python una funcion 'mas_repetir(lista) que reciba
una lista de numeros y que devuleva un conjunto que contenga
el que mas se repita dentro de la lista

mas_repetir([1, 7, 5, 8, 3, 6, 5, 9]) => 5
"""

"""
Si hay mas de un numero que se repita, el numero maximo de veces,
devera devolver un conjunto de todos ellos:

mas_repetir([1, 7, 5, 8, 3, 6, 5, 9, 5, 2, 2]) => (2, 5)

Si la lista esta vacia, devolver 'set()'
"""
def mas_repetir(lista):
    if not lista:
        return set()
    x = []
    y = []
    for i in lista:
        if i not in x:
            x.append(i)
    for i in x:
        if lista.count(i) > 1:
            y.append(i)
    return set(y)

def unicos(secuencia):
    def auxiliar(sec, acc):
        print(sec, "->", acc)
        if len(sec) == 0:
            return acc
        n = sec[0]
        if secuencia.count(n) == 1:
            acc.add(n)
        return auxiliar(sec[1:], acc)
    return auxiliar(secuencia, set())
