def cambia(l):
    print(l)
    l.append(99)

lista = [1, 2, 3]
cambia(lista)     # Imprime [1, 2, 3]
print(lista)      # Imprime [1, 2, 3, 99]
