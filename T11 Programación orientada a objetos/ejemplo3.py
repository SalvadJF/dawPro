class Usuario:
    def __init__(self, usuario, contrasenia, DNI) -> None:
        self._usuario = usuario
        self._contrasenia = contrasenia
        self._DNI = DNI

    def get_user(self):
        return f"El usuario es {self._usuario}"

    def get_DNI(self):
        return self._DNI

    def __eq__(self, objeto_importado) -> bool:
        return isinstance(objeto_importado, Usuario) and self._DNI == objeto_importado.get_DNI()

    def __hash__(self) -> int:
        return hash(self._usuario)

    def __repr__(self) -> str:
        return f'Usuario({repr(self._usuario)}, Contraseña *****, {self._DNI})'

    def set_user(self, contrasenia, usuario_nuevo):
        if self._contrasenia == contrasenia:
            self._usuario = usuario_nuevo
            return "Cambio de usuario exitoso"
        return "Contraseña invalida"
