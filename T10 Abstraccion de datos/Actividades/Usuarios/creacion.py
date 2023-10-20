"""
    Este programa modular permite la creacion de usuario y su modificacion

"""
# Modulos
usuarios = {}  # Diccionario para almacenar los usuarios y contraseñas creados

def hacer(opcion):
    """Devuelve la función que representa la opción elegida"""
    if opcion == 'crear':
        def crear_usuario():
            """Esta función crea un usuario y le da una contraseña

            Returns:
                tuple: una tupla con el nombre de usuario y la contraseña
            """
            usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            usuarios[usuario] = contrasena
            # Agregar el usuario y la contraseña al diccionario global
            return usuario, contrasena
        return crear_usuario
    elif opcion == 'modificar':
        def modificar_contrasena():
            """Esta función modifica la contraseña de un usuario existente

            Returns:
                tuple: una tupla con el nombre de usuario y la nueva contraseña
            """
            usuario = input("Ingrese el nombre de usuario: ")
            if usuario in usuarios:
                nueva_contrasena = input("Ingrese la nueva contraseña: ")
                usuarios[usuario] = nueva_contrasena
                # Actualizar la contraseña del usuario en el diccionario global
                return usuario, nueva_contrasena
            print('Usuario no encontrado')
            return None, None
        return modificar_contrasena
    print('Opción no válida')

while True:
    print('¡Bienvenido!')
    print('¿Quiere crear un nuevo usuario o cambiar una contraseña?')
    opcion = \
        input("Ingrese 'crear' para crear un usuario o 'modificar' para cambiar una contraseña: ")

    usuario=hacer(opcion)
    usuario()
