"""
En una empresa ha habido un fallo y necesitan implementar una función llamada
"ordenar_palabra(palabra)" que resuelva el siguiente problema.
El problema es que han realizado una encuesta, y al almacenar los datos en su base de datos,
los nombres de cada usuario se han "codificado" sin querer.
El programa de codificación realiza un intercambio de letras
por cada par que haya disponible en una palabra.
Por ejemplo:

* Si introducimos: Jose -> oJes
* Si introducimos: Irene -> rInee

Se puede observar que en el caso de que la longitud de la palabra sea impar,
el elemento desubicado queda invariante.

Por tanto, la función debe actuar en sentido inverso a la codificación realizada
en el formulario de forma errónea y devolver así una cadena con el resultado esperado.
En el caso de pasar como argumento de entrada a la función una cadena vacía,
se ha de devolver una cadena vacía.

"""

def ordenar_palabra(palabra):
    """Esta funcion recibe una palabra desordenada y la ordena alfabeticamente

    Args:
        palabra (str): la palabra en cuestion

    Returns:
        palabra_ordenada (str): la palabra ordenada alfabeticamente
    """
    if not palabra:
        # verificar si la palabra es una cadena vacia
        return ""
    palabra_lista = list(palabra)
    # convieter la cadena a lista
    # intercambiar pares consecutivos de letras
    for i in range(0, len(palabra_lista)-1, 2):
        palabra_lista[i], palabra_lista[i+1] = palabra_lista[i+1], palabra_lista[i]
    # volver a crear la cadena a partir de la lista
    palabra_ordenada = "".join(palabra_lista)

    return palabra_ordenada
