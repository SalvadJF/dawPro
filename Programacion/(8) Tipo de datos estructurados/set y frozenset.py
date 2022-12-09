#set devuelve un conjunto de tipo set.

ejemplo_set = set([4, 3, 2, 2, 4])

# es igual que poner {2, 3, 4}

#frozenset devuelve un conjunto de tipo frozenset.

ejemplo_frozen = frozenset([4, 3, 2, 2, 4])

# es igual que poner frozenset({2, 3, 4})

# se puede usar s.add(para añadir) y s.remove(para quitar) elementos

# tambien podemos usar expresiones generadoras

ejemplo3 = {x ** 2 for x in [1, 2, 3]}
