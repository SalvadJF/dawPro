"""Escribir en Python una función
recursiva llamada unicos(secuencia)
que reciba una secuencia de números
enteros en la que todos aparecen dos o más veces,
excepto dos de ellos que aparecen exactamente una vez
. La función deberá devolver un conjunto de tipo set
que contenga sólo esos dos elementos únicos."""
#No puedes usar while, ni expresiones generadoras


ejemplo = [1, 9, 8, 8, 7, 6, 1, 6]

"""
def unicos(sec):
    it = iter(sec)
    acc = 0
    x = next(it)
    if acc == 0:
        acc += 1
        if x == it:
            acc += 1
            del sec[x]
            unicos(sec)
        else:
            x != it
            acc = 0
            unicos(sec)
    return set(sec)


print(unicos(ejemplo))
"""
#Resuelto
def unicos(secuencia):
    def auxiliar(sec, acc):
        if len(sec) == 0:
            return acc
        n = sec[0]
        if secuencia.count(n) == 1:
            acc.add(n)
        return auxiliar(sec[1:], acc)
    return auxiliar(secuencia, set())
