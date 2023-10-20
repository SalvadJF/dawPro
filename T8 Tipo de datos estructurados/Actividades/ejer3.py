"""
3 Calcular pérdidas totales
¡Acabas de regresar a casa y descubres que han robado tu mansión! Dado un diccionario de
los artículos robados, devolver el monto total del robo (número). Si no se robó nada, devolver
la cadena "Lucky you!".

"""

perdidas = {"tv" : 30,"skate" : 20,"stereo" : 50,}
nada = {}
def robo(a):
    res = sum(a.values())
    if res == 0 or res is None:
        return print("Lucky you!")
    return  print(res)
#return sum(a.values()) or "Lucky you!"

robo(perdidas)
robo(nada)
