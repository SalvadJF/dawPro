"""
Escribir una función ahorcado(prueba) que juegue un turno del juego del ahorcado.
Para ello, la función recibe una cadena (el intento) con la palabra que el usuario
cree que es la que hay que averiguar (la solución).
La solución se encuentra almacenada en la primera línea del archivo de texto «ahorcado.txt».
La función deberá leer ese archivo y comprobar si el intento coincide con la solución.
En caso afirmativo, deberá mostrar por la salida el mensaje «¡Enhorabuena!».
En caso contrario, deberá mostrar la solución con las letras adivinadas
(es decir, las letras que aparecen en el intento), y las letras no
adivinadas sustituidas por un guión bajo.
Se supone que las letras son siempre mayúsculas y sin acentos.
"""

def ahorcado(intento):
    with open('ahorcado.txt') as f:
        solucion = f.readline().strip()
        if intento == solucion:
            print('!Enhorabuena!')
        else:
            for c in solucion:
                if c in intento:
                    print(c, end='')
                else:
                    print('_', end='')
        #Tambien se podria poner como print(c if c in intento else '_', end='')
