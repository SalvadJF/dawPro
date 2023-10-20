"""

Usa el módulo random para escribir programas que necesiten mostrar un comportamiento aleatorio:

a) La función random.randint(a,b) devuelve un número entero aleatorio entre a y

b) Úsala para escribir un programa que juegue a que el
usuario tenga que adivinar un número entre 1 y 100.

c) La función random.shuffle(x) ordena aleatoriamente la secuencia x.
Úsala para escribir un programa que pida al usuario cinco cadenas y
que luego las imprima en un orden aleatorio.

"""

import random

#a)
A = random.randint(1, 100)

print(A)

#b)
while True:
    a = input("Introduzca un numero: ")
    if a == A:
        print("Felicidades")
        break
    print("Intentalo otra vez")
