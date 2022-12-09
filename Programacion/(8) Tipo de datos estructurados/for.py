
"""for ⟨variable⟩(, ⟨variable⟩)* in ⟨iterable⟩:
      ⟨sentencia⟩"""

#es una forma mas sencilla de escribir esto
"""iterador = iter(⟨iterable⟩)
fin = False
while not fin:
        try:
                ⟨variable⟩(, ⟨variable⟩)*  = next(iterador)
        except StopIteration:
                fin = True
        else:
                ⟨sentencia⟩"""

#Ejemplo


def mostrar(l):
    for e in l:
        print(e)

mostrar([1, 2, 3, 4])

def mostrar2(l):
    for x, y in (l):
        print(x, y)
