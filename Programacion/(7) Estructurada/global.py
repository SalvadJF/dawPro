x = 4

def prueba():
    global x  # informa que la variable 'x' es global
    x = 5     # cambia el valor de la variable global 'x'

prueba()
print(x)  # imprime 5

def prueba2():
    global y  # informa que la variable 'y' (que aún no existe) es global
    y = 9     # se crea una nueva variable global 'y' que antes no existía

prueba2()
print(y)  # imprime 9
