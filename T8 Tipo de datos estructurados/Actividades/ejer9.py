"""
9 Obtener nombres de estudiantes
Crear una función que tome un diccionario de nombres de estudiantes y devuelva una lista de
nombres de estudiantes en orden alfabético."""

estudiantes = {"Student 1" : "Steve", "Student 2" : "Becky", "Student 3" : "John"}

def ordenar(a):
    return print(sorted(a.values()))

ordenar(estudiantes)
