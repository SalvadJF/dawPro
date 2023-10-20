class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos

    def __str__(self):
        return f"Cliente {self.__nombre} {self.__apellidos}"

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.__dni == other.__dni
        return False

    def __hash__(self):
        return hash(self.__dni)


class Cuenta:
    numero_cuentas = 0

    def __init__(self, titular):
        self.__titular = titular
        self.__numero = Cuenta.numero_cuentas + 1
        self.__saldo = 0
        self.__movimientos = []
        Cuenta.numero_cuentas += 1

    def __str__(self):
        return f"Cuenta número: {self.__numero}, con Titular: {self.__titular}"

    def __eq__(self, other):
        if isinstance(other, Cuenta):
            return self.__numero == other.__numero
        else:
            return False

    def __hash__(self):
        return hash(self.__numero)

    def imprimir_movimientos(self):
        for movimiento in self.__movimientos:
            print(movimiento)
        print(f"Saldo disponible: {self.__saldo}")


class Movimiento:
    def __init__(self, concepto, cantidad):
        self.__concepto = concepto
        self.__cantidad = cantidad

    @property
    def concepto(self):
        return self.__concepto

    @concepto.setter
    def concepto(self, concepto):
        if concepto not in ["Ingresar", "Retirar"]:
            raise ValueError("Concepto no válido")
        self.__concepto = concepto

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad no válida")
        self.__cantidad = cantidad

    def __str__(self):
        return f"Movimiento: {self.__concepto} de {self.__cantidad}"
