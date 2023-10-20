""" Ejercicio examen 3"""

#Debe ser recursiva e iterativa
#usaremos acumuladores para funciones iterartivas

alumnos = [
    {'nombre': 'Juan', 'media': 7.2},
    {'nombre': 'Antonio', 'media': 2.5},
    {'nombre': 'Maria', 'media': 8.5}
]

def aprobados_si_o_no(lista: list[dict]) -> list[tuple]:
    def auxiliar(dics):
    #acc acumula las tuplas
        if len(dics) == 0:
            return
        alum = dics[0]
        res.append((alum['nombre'], alum['media'] >= 4.5))
        auxiliar(dics[1:])
    res = []
    auxiliar(lista)
    return res


print(aprobados_si_o_no(alumnos))


def fact(n):
    def fact_iter(n, acc):
        if n == 0:
            return acc
        return fact_iter(n - 1, acc * n)
    return fact_iter(n, 1)
