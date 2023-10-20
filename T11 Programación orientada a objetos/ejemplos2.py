"""Recordemos el ejemplo del tema anterior en el que implementamos
    el tipo abstracto de datos Depósito mediante la siguiente función:
    pero esta vez usaremos la programacion orientada a objetos
"""
class Deposito:
    def __init__(self, fondos):
        self.fondos = fondos

    def retirar(self, cantidad):
        if cantidad > self.fondos:
            return 'Fondos insuficientes'
        self.fondos -= cantidad
        return self.fondos

    def ingresar(self, cantidad):
        self.fondos += cantidad
        return self.fondos

    def saldo(self):
        return self.fondos
