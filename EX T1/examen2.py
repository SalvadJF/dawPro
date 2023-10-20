"""Escribir en Python una función pura llamada str2dict(lista)
que reciba una lista de cadenas de la forma "X=Y" (sin espacios),
donde X es un valor hashable y único (es decir, que no se repite
como ningún otro valor de X en ninguna otra cadena de la lista) e Y es una cadena.
La función debe devolver un diccionario donde la clave de cada elemento
será la X y el valor asociado a dicha clave será la correspondiente Y."""

lista = (['perro=guau', 'gato=miau'])


#solucion

def str2dict(lis):
    res = {}
    for e in lis:
        k, v = e.split('=')
        res[k] = v
    return res

#2 solucion
def str2dict2(lis):
    return dict(e.split('=') for e in lis)
