f = open('carta.txt', 'r')
contenido = f.readlines()
f.close()

caracteres, lineas, palabras = 0, 0, 0

i = 0
while i < len(contenido):
    linea = contenido[i]
    caracteres += len(linea)
    lineas += 1
    palabras += linea.count(' ') + 1
    i += 1

f.close()
print(caracteres, lineas, palabras, 'carta.txt')
