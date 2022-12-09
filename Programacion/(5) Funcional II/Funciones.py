"""Ejercicios de funciones creadas con expresiones lambda"""
division_segura = lambda x, y: x / y if y != 0 else 'error'

maximo2 = lambda x, y: x if x >= y else y

maximo3 = lambda x, y, z: maximo2(x, maximo2(y, z))
"""maximo3 = lambda x, y, z: x if x >= y and x >= z else y if y >= x and y >= z else z"""
