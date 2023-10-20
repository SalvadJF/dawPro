"""
108. Se dispone de las siguientes secuencias de caracteres:
• Secuencia 1: e i k m p q r s t u v
• Secuencia 2: p v i u m t e r k q s
Con ellas, es posible codificar un texto convirtiendo cada letra de la secuencia 1 en
su correspondiente de la secuencia 2. El resto de los caracteres no se modifican. Las
secuencias se utilizan tanto para codificar mayúsculas como minúsculas, mostrando
siempre la codificación en minúsculas.
Por ejemplo, la palabra «PaquiTo» se codifica como «matqvko».
Escribir un programa que codifique un texto. Para ello, se debe implementar la siguiente
función:
Pre : len(𝑐) = 1
codifica(𝑠𝑒𝑐1: str, 𝑠𝑒𝑐2: str, 𝑐: str) -> str

Post : len(codifica(𝑠𝑒𝑐1, 𝑠𝑒𝑐2, 𝑐)) = 1 ∧
𝑐 ∈ 𝑠𝑒𝑐1 → codifica(𝑠𝑒𝑐1, 𝑠𝑒𝑐2, 𝑐) = el correspondiente de 𝑐 en 𝑠𝑒𝑐2
𝑐 ∉ 𝑠𝑒𝑐1 → codifica(𝑠𝑒𝑐1, 𝑠𝑒𝑐2, 𝑐) = 𝑐
que devuelve el carácter 𝑐 codificado según las secuencias 1 y 2 que se le pasan.

"""
SEC1 = 'eikmpqrstuv'
SEC2 = 'pviumterkqs'

def codifica(sec1: str, sec2: str, c: str) -> str:
    i = sec1.find(c)
    return c if i == -1 else sec2[i]
"""
if i == -1:
    return c
return sec2[i]
"""

entrada = input('Introduzca el texto a codificar: ').lower()
salida = []
for e in entrada:
    salida.append(codifica(SEC1, SEC2, e))
salida = ''.join(salida)
#salida = ''.join([codifica(SEC1, SEC2, e) for e in entrada])
print('El texto codificado es: ', salida)
