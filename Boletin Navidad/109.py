"""
109. Un anagrama es una palabra que resulta del cambio del orden de los caracteres de
otra. Ejemplos de anagramas para la palabra roma son: amor, ramo o mora. Escribir un
programa que solicite al usuario dos palabras e indique si son anagramas una de otra.
"""

def es_anagrama(p1: str, p2: str) -> bool:
    return sorted(p1) == sorted(p2)
