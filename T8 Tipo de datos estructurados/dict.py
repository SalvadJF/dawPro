v1 = {}                                          # diccionario vacío
v2 = dict()                                      # también diccionario vacío
v1 == v2
#True
a = {'uno': 1, 'dos': 2, 'tres': 3}              # literal
b = dict(uno=1, dos=2, tres=3)                   # argumentos con nombre
c = dict([('dos', 2), ('uno', 1), ('tres', 3)])  # lista de tuplas
d = dict({'tres': 3, 'uno': 1, 'dos': 2})        # innecesario
e = dict(zip(['uno', 'dos', 'tres'], [1, 2, 3])) # con dos iterables
a == b and b == c and c == d and d == e          # todos son iguales
#True
