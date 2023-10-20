class credenciales:
    def __init__(self, usuario,contrasena) -> None:
        # Usamos el __ delante del objeto para marcarlo como que solo se muestre el
        self.__usuario = usuario
        self.contrasena = contrasena
    def  consultar (self):
        return self.__usuario


usuario1 = credenciales("Pepe", 1234)

print(usuario1.consultar())
