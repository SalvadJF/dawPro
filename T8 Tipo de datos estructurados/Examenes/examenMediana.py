#Ejercicios del examen

dicionario = {'nombre': 'Juan', 'notas': [7.5, 3.5, 9.0, 8.6]}

#devuelva {'nombre': 'Juan', 'notas': [7,5, 3,5, 9.0, 8.6]}, 'mediana': 8.1)

def mediana(dicionario):
    res = dicionario['notas']
    if res == len(res % 2 == 0):
        x = sorted(())
    else:
        x = sorted((len(res) // 2))
    o = {'mediana': x}
    return dicionario.update(o)

#Resuelto
#Sorted crea una lista nueva, por tanto sigue siendo pura
dic = {'nombre': 'Juan', 'notas': [7.5, 3.5, 9.0, 8.6]}
def medianasol(dic):
    """Ejercicio 2 del examen"""
    res = dic.copy()
    notas = sorted(res['notas'])
    l = len(notas)
    mitad = l // 2
    if l % 2 == 0:
        mediana = notas [mitad - 1] + notas(mitad) / 2
    else:
        mediana = notas[mitad]
    res['mediana'] = round(mediana, 1)
    return res
