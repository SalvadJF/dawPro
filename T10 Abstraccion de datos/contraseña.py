def pareja(x, y):
    """Devuelve una función que representa una pareja."""
    def get(indice):
        if indice == 0:
            return x
        elif indice == 1:
            return y

    return get

def select(p, i):
    """Devuelve el elemento situado en el índice i de la pareja p."""
    return p(i)
