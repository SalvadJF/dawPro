class Articulo:
    def __init__(self, nombre, cantidad):
        self.__nombre = nombre
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f"Nombre del artículo: {self.__nombre} Cantidad del artículo: {self.__cantidad} [uds]"

class Gestion_articulo:
    articulos = []

    @staticmethod
    def alta_articulo(nombre):
        for articulo in Gestion_articulo.articulos:
            if articulo.get_nombre() == nombre:
                raise NotImplementedError("El artículo ya existe")
        Gestion_articulo.articulos.append(Articulo(nombre, 0))

    @staticmethod
    def agregar_cantidad_articulo(nombre, cantidad):
        for articulo in Gestion_articulo.articulos:
            if articulo.get_nombre() == nombre:
                articulo.set_cantidad(articulo.get_cantidad() + cantidad)
                break
        raise NotImplementedError("El artículo no existe")

    @staticmethod
    def retirar_cantidad_articulo(nombre, cantidad):
        for articulo in Gestion_articulo.articulos:
            if articulo.get_nombre() == nombre:
                if articulo.get_cantidad() - cantidad < 0:
                    raise NotImplementedError("No hay suficiente stock")
                else:
                    articulo.set_cantidad(articulo.get_cantidad() - cantidad)
                    break
        else:
            raise NotImplementedError("El artículo no existe")

    @staticmethod
    def imprimir_articulos():
        for articulo in Gestion_articulo.articulos:
            print(articulo)
        print(f"Total de artículos dados de alta: {len(Gestion_articulo.articulos)}")

class Albaran:
    num_entrada = 0

    def __init__(self, id_albaran, articulo, cantidad):
        Albaran.num_entrada += 1
        self.__num_entrada = Albaran.num_entrada
        self.__id_albaran = id_albaran
        self.__articulo = articulo
        self.__cantidad = cantidad
        try:
            Gestion_articulo.agregar_cantidad_articulo(self.__articulo, self.__cantidad)
        except NotImplementedError as e:
            print(e)
            Albaran.num_entrada -= 1
            raise ValueError("No se ha podido crear el albarán")

    def get_num_entrada(self):
        return self.__num_entrada

    def get_id_albaran(self):
        return self.__id_albaran

    def set_id_albaran(self, id_albaran):
        self.__id_albaran = id_albaran

    def get_articulo(self):
        return self.__articulo

    def set_articulo(self, articulo):
        self.__articulo = articulo

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f"Numero de entrada: {self.__num_entrada} Id del albarán: \
            {self.__id_albaran} Artículo: {self.__articulo} Cantidad: {self.__cantidad}"

    @staticmethod
    def listar_albaranes():
        for albaran in Albaran.albaranes:
            print(albaran)

Albaran.albaranes = []
