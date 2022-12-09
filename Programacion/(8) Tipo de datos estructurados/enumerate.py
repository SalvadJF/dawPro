#enumerate entrega un (indice[posicion en la lista],valor)

# i = indice | e = elemento
for i, e in enumerate(['a', 'b', 'c']):
    print('El elemento en la posición ' + str(i) + ' es ' + str(e))

#Ejemplo de sumar los elementos de una lista
lista = [1, 2, 3, 4]
for i, e in enumerate(lista):
    lista[i] = e + 1
print(lista)

#Pasar a mayusculas
letras = ['a', 'b', 'c', 'd']
for i, e in enumerate(letras):
    letras[i] = e.upper()
print(letras)

#los archivos abiertos tambien so iterables
with open('archivo.txt') as f:
    for linea in f:
        print(linea)
