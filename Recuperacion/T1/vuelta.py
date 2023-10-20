"""
Escribir en Python una fucnión llamada "vuelta(precio,entrega)"
que muestre por la salida estándar la cantidad a devolver,
indicando en cada elemento de la lista una cadena que indique el número de monedas
y su cantidad para cada una de las monedas a devolver.
Este cálculo se ha de realizar teniendo en cuenta que la
cantidad de dinero (número de billetes y monedas) debe ser mínimo.

Observación: Considerar las siguientes cantidades de dinero 500, 200, 50, 20, 10, 5, 2. 1 €.
Esto nos lleva a que el dominio de la función de entrada y salida es el de los números enteros.

En el caso de introducir una cantidad de entrega menor que el precio,
la función no debe mostrar nada.

Por ejemplo:
>>>> vuelta(12, 60)
['2->20', '1->5', '1->2', '1->1']

"""
""" SJF """
def vuelta(precio, entrega):
    """Esta funcion muestra un pago y cuanto devuelve en monedas.

    Args:
        precio (int): El precio del objeto
        entrega (int): Lo que paga el cliente

    Returns:
        resultado (list): devuelve una lista con las monedas que se le devuelve al usuario
    """
    cambio = entrega - precio

    if cambio < 0:
        return []

    cantidades = [500, 200, 50, 20, 10, 5, 2, 1]
    resultado = []

    for moneda_val in cantidades:
        cant_moneda = cambio // moneda_val
        if cant_moneda > 0:
            resultado.append(f"{cant_moneda}->{int(moneda_val)}")

            cambio -= cant_moneda * moneda_val

    return print(resultado)



"""
Test = vuelta(12,60)
Esperado = ['2->20', '1->5', '1->2', '1->1']
Se obtuvo = ['2->20.00', '1->5.00', '1->2.00', '1->1.00']
"""
