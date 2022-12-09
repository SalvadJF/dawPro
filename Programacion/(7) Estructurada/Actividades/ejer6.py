num = int(input('introduzca el numero: '))

"""
print(num, 'x 0', '=', 0 * num)
print(num, 'x 1', '=', 1 * num)
print(num, 'x 2', '=', 2 * num)
print(num, 'x 3', '=', 3 * num)

print(tuple(map(lambda x: num * x, range(11))))
"""

tuple(print(num, 'x',  x, '=', x * num) for x in range(11))
