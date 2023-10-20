class Cliente:
    def __init__(self, DNI, nombre, apellidos):
        self.set_DNI(DNI)
        self.set_nombre(nombre)
        self.set_apellidos(apellidos)

    def set_DNI(self, DNI):
        self.__DNI = DNI

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellidos(self,apellidos):
        self.__apellidos = apellidos

    def get_DNI(self):
        return self.__DNI

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def __repr__(self):
        return f"Cliente: ({repr(self.get_DNI)}, (repr{self.get_nombre}), \
            (repr{self.get_apellidos}))"

    def __eq__(self, otro_cliente):
        if isinstance(otro_cliente, Cliente):
            return self.get_DNI() == otro_cliente.get_DNI()
        raise NotImplementedError("No coincide el tipo de instancia")

    def __hash__(self):
        return hash(self.get_DNI)

    def __str__(self):
        return f"Nombre del cliente : {self.get_nombre} {self.get_apellidos} con DNI {self.get_DNI}"

class Cuenta:
    __numero = 0

    def __init__(self, titular, movimientos=None):

        self.set_numero()
        self.set_titular(titular)
        self.set_saldo(0)

        if movimientos is None:
            self.__movimientos = []
        self.__movimientos = movimientos

    def set_numero(self):
        Cuenta.__numero += 1
        self.__numero = Cuenta.__numero

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    def get_movimientos(self):
        return self.__movimientos

    def __eq__(self, otra_cuenta):
        if not isinstance(otra_cuenta, Cuenta):
            raise NotImplementedError("No coinciden los tipos de datos pasados")
        return self.get_numero() == otra_cuenta.get_numero()

    def __hash__(self):
        return hash(self.__numero)

    def __repr__(self):
        return f'Cuenta({self.get_titular()}), {self.get_movimientos()}'


    def __str__(self):
        return f"Cuenta: {self.__numero}, Titular: {self.__titular}, \
        Movimientos: {self.__movimientos}, Saldo: {self.__saldo}"

class Movimiento:
    def __init__(self, concepto, cantidad):
        self.set_concepto(concepto)
        self.set_cantidad(cantidad)

    def set_concepto(self, concepto):
        if concepto in ("Retirar", "Ingresar"):
            self.__concepto = concepto
        raise ValueError("Concepto Errorneo")

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_concepto(self):
        return self.__cantidad

    def get_cantidad(self):
        return self.__cantidad

    def __str__(self):
        return f"Movimiento: {self.__concepto}, Cantidad: {self.__cantidad}"

    def operacion(self, concepto, cantidad , cuenta):
        if concepto == "Retirar" and cantidad > Cuenta.get_saldo():
            raise ValueError("No hay saldo suficiente")
        elif concepto == "Retirar":
            return Cuenta.set_saldo(cuenta.get_saldo() - cantidad)
        else concepto == "Ingresar":
            return Cuenta.set_saldo(cuenta.get_saldo() + cantidad)
        raise ValueError("Concepto Erroneo")
