"""
1 Devolver el último elemento
Crear una función que devuelva el valor del último elemento de una lista o cadena.

"""
l = [1, 2, 'a', 'g']
def ultimo_elemento(a):
    try:
        return (a[-1])
    except IndexError:
        return None

ultimo_elemento(l)
ultimo_elemento('hola')
