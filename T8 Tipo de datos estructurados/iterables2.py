r = range(300)

res = map(lambda x: x ** 2, r)

#para uno a uno
next(res)

#para todos a la vez
list(res)

#Tambien funcionan en expresiones generadoras

cuadrados = (x ** 2 for x in range(1, 10))

#para uno a uno
next(cuadrados)

#para todos a la vez
list(cuadrados)
