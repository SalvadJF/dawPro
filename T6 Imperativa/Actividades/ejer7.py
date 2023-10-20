x = int(input('Introduzca el primer numero: '))
y = int(input('Introduzca el segundo numero: '))
Comparacion = lambda x , y: 'Si' if x == y else 'No'
print((Comparacion(x,y)) , 'son iguales')
