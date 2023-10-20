class Vehiculo:
    """Ejemplo de un vehiculo para practicar las herencias"""
    def __init__(self, marca, modelo):
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.arrancado = False

    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_arrancado(self):
        self.arrancado = True

    def set_parado(self):
        self.arrancado = False

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_estado(self):
        return self.arrancado

    def __repr__(self) -> str:
        return f" Vehiculo({self.get_marca()!r}, {self.get_modelo()!r})"

    def __str__(self) -> str:
        return f"Marca: {self.get_marca()}, Modelo: {self.get_modelo()}\
            y el vehiculo está: {'Arracando' if self.get_estado is True else 'Parado'}"

class Moto(Vehiculo):
    hcaballito=""

    def __init__(self, marca, modelo, matricula):
        super().__init__(marca, modelo)
        self.matricula = matricula
        self.set_arrancado()

    def caballito(self):
        self.hcaballito ="Voy haciendo el caballito"

    def estado(self):
        return self.hcaballito
