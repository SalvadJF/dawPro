""" Examen T2 : Salvador Jimenez Fernandez"""


class Articulo:
    """Es esta clase guardamos los nombres y candidad de nuestros articulos"""
    def __init__(self, nombre, cantidad):
        self.set_nombre(nombre)
        self.set_cantidad(cantidad)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def __repr__(self):
        return f'Articulo: ({self.get_nombre()}),({self.get_cantidad()})'

    def __str__(self):
        return f'<<Nombre del articulo {self.get_nombre()}\
            >> <<Cantidad del articulo {self.get_cantidad()}>>'



class Gestion_articulo:
    """En esta clase se realizan las funciones para añadir articulos o cantidades"""
    def __init__(self):
        """ Los articulos que creamos los almacenamos dentro de la clase"""
        self.articulos = []

    def alta_articulo(self, nombre):
        """ Dar de alta un articulo"""
        if nombre in self.articulos:
            raise NotImplementedError("El articulo ya esta de alta")
        cantidad = 0
        self.articulos.append(Articulo(nombre, cantidad))
        print(f"Artículo {nombre} dado de alta con éxito.")


    def agregar_cantidad_articulo(self, nombre, cantidad):
        """ Agregamos cantidad a un articulo ya existente"""
        for articulo in self.articulos:
            if articulo.get_nombre() == nombre:
                articulo.set_cantidad(articulo.get_cantidad() + cantidad)
                print(f"{cantidad} unidades del artículo {nombre} añadidas con éxito.")
                return
        print(f"No se ha encontrado ningún artículo con el nombre {nombre}.")

    def retirar_cantidad_articulo(self, nombre, cantidad):
        """Retiramos cantidad a un articulo ya existente"""
        for articulo in self.articulos:
            if articulo.get_nombre() == nombre:
                if articulo.get_cantidad() >= cantidad:
                    articulo.set_cantidad(articulo.get_cantidad() - cantidad)
                    print(f"{cantidad} unidades del artículo {nombre} retiradas con éxito.")
                else:
                    print(f"No hay suficientes unidades del artículo {nombre}.")
                return
        print(f"No se ha encontrado ningún artículo con el nombre {nombre}.")

    def imprimir_articulos(self):
        """Imprime el articulo y sus cantidades existentes"""
        if len(self.articulos) == 0:
            print("No hay artículos dados de alta.")
        else:
            print("Listado de artículos:")
            for articulo in self.articulos:
                print(f"- {articulo.get_nombre()}: {articulo.get_cantidad()} unidades")


class Albaran:
    """Esta clase tiene la funcion de crear Albaranes"""
    num_entrada = 0
    lista_albaranes = []

    def __init__(self, id_albaran, articulo, cantidad):
        Albaran.num_entrada += 1
        self.set_num_entrada(Albaran.num_entrada)
        self.set_id_albaran(id_albaran)
        self.set_articulo(articulo)
        self.set_cantidad(cantidad)
        Albaran.lista_albaranes.append(self)


    def set_num_entrada(self, num_entrada):
        self.__num_entrada = num_entrada

    def get_num_entrada(self):
        return self.__num_entrada

    def set_id_albaran(self, id_albaran):
        self.__id_albaran = id_albaran

    def get_id_albaran(self):
        return self.__id_albaran

    def set_articulo(self, articulo):
        self.__articulo = articulo

    def get_articulo(self):
        return self.__articulo

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def get_cantidad(self):
        return self.__cantidad

    def __repr__(self):
        return f'{self.get_id_albaran()} -> Albaran Nª {self.get_num_entrada()} \
            ; Articulo: {self.get_articulo}, {self.get_cantidad()} [uds]'

    def __str__(self):
        return f'ID de Albaran: {self.get_id_albaran()}; Articulo: \
            {self.get_articulo()}, {self.get_cantidad()} [uds]'

    def listar_albaranes(self):
        for albaran in Albaran.lista_albaranes:
            print(albaran.__repr__())
