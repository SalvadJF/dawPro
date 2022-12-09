j = 0
s = "string"
while j < len(s):
    val = s[j]
    j += 1
    if val == "i":
        break
    print(val)
print("Fin")

"""
usar el break es una violacion de los principios
de la programcion estructurada por tener 2 salidas,
aun asi se usa por ser util.
se pude considerar un boton de 'emergencia'
"""
