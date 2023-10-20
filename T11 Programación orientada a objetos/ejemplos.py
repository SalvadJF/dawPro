# Ejemplo 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)
print(persona1.nombre)
persona2.saludar()

# Ejemplo 2
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass   # no hace nada por sí solo

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

perro1 = Perro("Fido")
gato1 = Gato("Garfield")
perro1.hacer_sonido()
gato1.hacer_sonido()

# Ejemplo 3
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

figuras = [Cuadrado(4), Circulo(3), Cuadrado(2)]
for figura in figuras:
    print(figura.area())
