"""
1) Realizar un programa en Python que se llame "encriptar_palabra(palabra)",
que le introduzcas una palabra y que la transcriba a su homologa encriptada.
Para ello, hay que conocer que para cada letra del abecedario se ha de obtener
convertir en una específica encriptada con la siguiente relación.

El formato del abecedario es: a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z
El formato encriptado es:     q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,ñ,z,x,c,v,b,n,m

Como ejemplo:

>>> encriptar_palabra("hola")
"ihsq"

2) Escribir una función que sume los elementos de una lista de forma recursiva,
la cual se denomina "suma(lista)".

Ejemplo:
>>> lista = [1, 2, 3, 4, 5]
>>> sumar(lista)
15
"""
#1

def encriptar_palabra(palabra):
    abecedario = {'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't', 'f': 'y', 'g': 'u',
                  'h': 'i', 'i': 'o', 'j': 'p', 'k': 'a', 'l': 's', 'm': 'd', 'n': 'f',
                  'ñ': 'g', 'o': 'h', 'p': 'j', 'q': 'k', 'r': 'l', 's': 'ñ', 't': 'z',
                  'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'}
    palabra_encriptada = ""
    for letra in palabra:
        if letra.lower() in abecedario:
            palabra_encriptada += abecedario[letra.lower()]
        else:
            palabra_encriptada += letra
    return palabra_encriptada

#2

def sumar(lista):
    if len(lista) == 1:
        return lista[0]
    return lista[0] + sumar(lista[1:])
