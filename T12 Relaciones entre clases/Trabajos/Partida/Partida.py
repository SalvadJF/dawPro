class Grupo:

    """Esto es un ejemplo de un grupo de jugadores para una partida de rol"""

    __numeroGrupo = 0

    def __init__(self, nombreG):
        self.set_numeroGrupo()
        self.set_nombreGrupo(nombreG)

    def set_numeroGrupo(self):
        Grupo.__numeroGrupo += 1
        self.__numeroGrupo = Grupo.__numeroGrupo

    def set_nombreGrupo(self, nombreG):
        self.__nombreGrupo = nombreG

    def get_numeroGrupo(self):
        return self.__numeroGrupo

    def get_nombreGrupo(self):
        return self.__nombreGrupo

    def __repr__(self) -> str:
        return f'Grupo({self.get_nombreGrupo()!r}, {self.get_numeroGrupo()!r})'

    def __str__(self) -> str:
        return f'Grupo nª {self.get_numeroGrupo()}, Nombre {self.get_nombreGrupo()}'



class Jugador:

    """Esta es una subclase que representa los jugadores del grupo"""

    __numeroJugador = 0

    def __init__(self, nombreJ):
        self.set_numeroJugador()
        self.set_nombreJugador(nombreJ)

    def set_numeroJugador(self):
        Jugador.__numeroJugador += 1
        self.__numeroJugador = Jugador.__numeroJugador

    def set_nombreJugador(self, nombreJ):
        self.__nombreJugador = nombreJ

    def get_numeroJugador(self):
        return self.__numeroJugador

    def get_nombreJugador(self):
        return self.__nombreJugador

    def __repr__(self) -> str:
        return f'Jugador({self.get_numeroJugador()!r}, {self.get_nombreJugador()!r})'

    def __str__(self) -> str:
        return f'Jugador nª {self.get_numeroJugador()}, Nombre : {self.get_nombreJugador()}'

class Gestion(Grupo, Jugador):

    __GRUPOS = []
    __JUGADORES = []

    @staticmethod
    def crear_grupo(nombreG):
        for grupo in Gestion.__GRUPOS:
            if grupo.get_nombreGrupo() == nombreG:
                raise ValueError("El grupo ya existe")
        Gestion.__GRUPOS.append(nombreG)
        f'Grupo {nombreG} creado'

    @staticmethod
    def borrar_grupo(nombreG):
        for grupo in Gestion.__GRUPOS:
            if grupo.get_nombreGrupo().find(nombreG) is False:
                raise ValueError("El grupo no existe")
        Gestion.__GRUPOS.remove(nombreG)

    @staticmethod
    def crear_jugador(nombreJ):
        for jugador in Gestion.__JUGADORES:
            if jugador.get_nombreJugador() == nombreJ:
                raise ValueError("El Jugador ya existe")
        Gestion.__JUGADORES.append(nombreJ)
        f'Jugador {nombreJ} creado'

    @staticmethod
    def borrar_jugador(nombreJ):
        for jugador in Gestion.__JUGADORES:
            if jugador.get_nombreJugador().find(nombreJ) is False:
                raise ValueError("El Jugador no existe")
        Gestion.__JUGADORES.remove(nombreJ)

    @staticmethod
    def agregar_miembros(nombreG, nombreJ):
        for grupo in Gestion.__GRUPOS:
            if grupo.get_nombreGrupo() == nombreG:
                for jugador in Gestion.__JUGADORES:
                    if jugador.get_nombreJugador() == nombreJ:
                        grupo.append(jugador)
                        return f'Jugador {nombreJ} añadido al grupo {nombreG}'
        raise ValueError("El grupo o el jugador no existen")

    @staticmethod
    def eliminar_miembros(nombreG, nombreJ):
        for grupo in Gestion.__GRUPOS:
            if grupo.get_nombreGrupo() == nombreG:
                for jugador in Gestion.__JUGADORES:
                    if jugador.get_nombreJugador() == nombreJ:
                        grupo.remove(jugador)
                        return f'Jugador {nombreJ} fue eliminado del grupo {nombreG}'
        raise ValueError("El grupo o el jugador no existen")

    @staticmethod
    def listar_grupos():
        print("*"*50)
        for grupo in Gestion.__GRUPOS:
            print(grupo)
        print()
        print("*"*50)

    @staticmethod
    def listar_jugadores():
        print("*"*50)
        for jugador in Gestion.__JUGADORES:
            print(jugador)
        print()
        print("*"*50)

    @staticmethod
    def listar_participantes(nombreG):
        print("*"*50)
        for grupo in Gestion.__GRUPOS:
            if grupo.get_nombreGrupo() == nombreG:
                for jugador in grupo:
                    print(jugador)
        print()
        print("*"*50)
