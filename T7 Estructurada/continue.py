j = 0
s = "string"
while j < len(s):
    val = s[j]
    j += 1
    if val == "i":
        continue
    print(val)
print("Fin")

"""tambien es una violacion de la programacion estructurada
por ser un salto, pero esta por conveniencia,por estar controlado"""
