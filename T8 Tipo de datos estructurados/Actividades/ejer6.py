"""
6 Añade su nombre
Dados tres argumentos (un diccionario obj, una clave name y un valor value) devolver un
diccionario con ese nombre y valor (como pares clave-valor)"""

ejemplo = [{}, "Brutus", 300]

def crear(obj, name, value):
    res = obj.copy()
    res[name] = value
    return res
