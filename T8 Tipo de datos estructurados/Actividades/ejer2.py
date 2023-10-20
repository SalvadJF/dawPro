"""
2 Asignar personas a profesiones
Tienes dos listas. Una muestra los nombres de las personas (names), mientras que el otro
muestra sus profesiones (jobs). Tu tarea es crear un diccionario que muestre a cada persona
con su respectiva profesión.

"""
names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]

def asignar(a, b):
    return print(dict(zip(a, b)))

asignar(names, jobs)
