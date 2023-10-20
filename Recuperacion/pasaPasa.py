"""
Escribir una funcion pasa_pasa() que manipule dos numeros enteros
suprimiendo la ultima cifra del primero y añadiendola al final del segundo

Usando esa funcion, escribir la funcion invierte() que invierte un numero
(partiendo del propio numero y de otro con valor inicial cero) a base
de repertir la operacion pasa_pasa() cuantas veces sea necesario

Ambas funciones deben recibir como argumento una lista llamda numeros con los dos numeros
sobre los que operan y deben cambiar dicha lista

Ademas la funcion invierte() debe mostrar cada paso del proceso, de la siguiente forma.

[12345, 0]
[1234, 5]
[123, 54]
[12, 543]
[1, 5432]
[0, 54321]
"""
def pasa_pasa(numeros: list):
    primero, segundo = numeros
    ultimo_digito = primero % 10
    primero //= 10
    segundo = segundo * 10 + ultimo_digito
    numeros[0], numeros[1] = primero, segundo

def invierte(numeros: list):
    while numeros[0] > 0:
        print(numeros)
        pasa_pasa(numeros)
    print(numeros)

a = [12345, 0]
invierte(a)
