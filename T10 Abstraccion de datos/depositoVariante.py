def deposito(fondos):
    def retirar(cantidad):
        nonlocal fondos
        if cantidad > fondos:
            return 'Fondos insuficientes'
        fondos -= cantidad
        return fondos

    def ingresar(cantidad):
        nonlocal fondos
        fondos += cantidad
        return fondos

    def saldo():
        return fondos

    dic = {'retirar': retirar, 'ingresar': ingresar, 'saldo': saldo}

    def despacho(mensaje):
        if mensaje in dic:
            return dic[mensaje]
        raise ValueError('Mensaje incorrecto')

    return despacho


"""

>>> retirar(25)
75
>>> ingresar(200)
275
>>> saldo()
275
"""
