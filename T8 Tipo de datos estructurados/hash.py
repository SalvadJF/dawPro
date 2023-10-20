#Si x == y, entonces debe cumplirse que hash(x) == hash(y).

"""
>>> hash('hola')
6290906884732116299

>>> hash(5)
5

>>> hash((1, 2, 3))
529344067295497451

# las listas no son hashables
>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
"""
