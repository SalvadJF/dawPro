"""
113. Realizar el juego del ahorcado. Las reglas del juego son:
a. El jugador A teclea una palabra, sin que el jugador B la vea.
b. Ahora se le muestran tantos guiones como letras tenga la palabra secreta. Por
ejemplo, para «hola» se mostraría «----».
c. El jugador B intentará acertar, letra a letra, la palabra secreta.
d. Cada acierto muestra la letra en su lugar, y las letras no acertadas seguirán ocul-
tas como guiones. Siguiendo con el ejemplo anterior, y suponiendo que se ha
introducido la «o», la «j» y la «a», se mostrará «-o-a».
e. El jugador B sólo tiene 7 intentos.
f. La partida terminará al acertar todas las letras que forman la palabra secreta (gana
el jugador B) o cuando se agoten todos los intentos (gana el jugador A)
"""
import random

NUM_INTENTOS = 7

with open('/usr/share/dict/words') as f:
    palabras = f.readlines()

secreta = random.choice(palabras).strip()
tabla = str.maketrans({'á' : 'a', 'é' : 'e', 'í' : 'i', 'ó' : 'o', 'ú' : 'u'})
secreta = secreta.translate(tabla)
print('-' * len(secreta))

intentos = []
total_intentos = 2 * len(secreta)
for num_intento in range(1, total_intentos +1):
    letra = input(f'(Intento{num_intento}) de {total_intentos} Introduzca una letra: ')
    if letra not in intentos:
        intentos.append(letra)
    acertado = True
    for c in secreta:
        if c in intentos:
            print(c, end='')
        else:
            acertado = False
            print('-', end='')
    print()
    if acertado:
        print('!Enhorabuena¡')
        break
