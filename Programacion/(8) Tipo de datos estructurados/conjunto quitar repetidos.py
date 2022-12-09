def quitar_repetidos(l):
    res = list(set(l))
    res.sort()
    return res

print(quitar_repetidos([1, 2, 2 ,2 ,3 ,3 ,4 ,4 ,6 ,6]))
