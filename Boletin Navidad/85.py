"""
85. Definir la función sin_repetidos que construye y devuelve una lista de longitud
apropiada, con los elementos de la lista original donde se han eliminado los datos repetidos.

"""


def sin_repetidos(lst: list) -> list:
    res = []
    for e in lst:
        if e not in res:
            res.append(e)
    return res
