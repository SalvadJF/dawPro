#Esta funcion invierte el key y el valor de un dicionario


def invertir(dicc):
    res = {}
    for x, y in dicc.items():
        res[y] = x
    dicc = res
    return res
