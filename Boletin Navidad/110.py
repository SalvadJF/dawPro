"""
110. Implementar el juego del anagrama, que consiste en que un jugador escribe una palabra
y el programa muestra un anagrama suyo generado al azar. A continuación, otro jugador
tiene que acertar cuál es el texto original. El programa no debe permitir que el texto
introducido por el primer jugador sea la cadena vacía. Por ejemplo, si el primer jugador
escribe «teclado», el programa muestra como pista un anagrama al azar, digamos,
«etcloda».
"""
import random
def generar_anagrama(p: str) -> str:
    return ''.join(random.sample(p, k=len(p)))
