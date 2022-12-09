#Iterables

"""
>>> lista = [1, 2, 3, 4]
>>> it = iter(lista)
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
4
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
"""
"""def mostrar(l):
    i = 0
    while i < len(l):
        print(l[i])
        i += 1"""

def mostrar(l):
    it = iter(l)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
