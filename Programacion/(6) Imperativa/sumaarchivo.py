f = open('suma.txt', 'r+')
lineas = f.readlines()
x = int(lineas[0].strip())
y = int(lineas[1].strip())
suma = x + y
f.write(str(suma) + '\n')
f.close()
