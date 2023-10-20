"""
⟨definición_función⟩ ::=
def ⟨nombre⟩([⟨lista_parámetros⟩]):
      ⟨cuerpo⟩


donde:
⟨lista_parámetros⟩ ::= identificador [, identificador]*
⟨cuerpo⟩ ::= ⟨sentencia⟩
      """


def saluda(persona):
    print('Hola', persona)
    quiensoy()
    print('Encantado de saludarte')

def despide():
    print('Hasta luego, Lucas')

def quiensoy():
    print('Me llamo Ricardo')

"""Ejemplo"""
saluda('Pepe')
print('El gusto es mío')
saluda('Juan')
despide()
print('Sayonara, baby')
