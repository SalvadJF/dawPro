"""
Escribir en Python una función recursiva llamada
"numeros_perfectos(numeros)" que devuelva un conjunto con todos los números perfectos.
Un número perfecto es aquel que es igual a la suma de sus divisores, sin tener en cuenta el 1.

6 es perfecto, pues 6 = 1 + 2 + 3

Recordar que un número es divisor, para aquellos
que al utilizarlos para dividir a otro, su resultado es exacto, o dicho de otro modo, el resto es 0.

Por ejemplo: Resto de 6/3 = 0, Resto de 6/2 = 0, Resto de 6/1 = 0, sin embargo, el resto de 6/4 = 2.
Por tanto, sólo son divisores de 6 en este ejemplo, el 3, 2 y el 1.

Ejemplo de uso:
numeros_perfectos([1,3,5,6,10,28]) -> {28,6}


Importante:

La función debe ser pura.
La llamada a la función debe provocar la ejecución de una
función recursiva que genere un proceso iterativo.
No se puede usar ningún bucle while, for, definiciones por comprensión ni expresiones generadoras.

Por ejemplo:
Test 	Resultado

print(numeros_perfectos([1,3,5,6,10]))



{6}

"""
""" SJF """
def divisores(num):
    """Funcion que comprueba si el numero es divisor

    Args:
        num (int): El numero a comprobar

    Returns:
        boolean : Devuelve TRUE o FALSE dependiendio si es divisor o no
    """
    return [i for i in range(2, num) if num % i == 0]


def es_perfecto(num):
    """Funcion que comprueba si el numero es perfecto

    Args:
        num (int): El numero a comprobar

    Returns:
        boolean: Devuelve TRUE o FALSE dependiendo si es perfecto o no
    """
    return sum(divisores(num)) + 1 == num


def numeros_perfectos(numeros):
    """Función recursiva que devuelve un conjunto con todos los números perfectos en una lista
    de números dada.

    Args:
        numeros (list): La lista con los numeros a comprobar

    Returns:
        list: Los numeros perfectos de la lista
    """
    if not numeros:
        return set()
    num = numeros[0]
    otros_perfectos = numeros_perfectos(numeros[1:])
    if es_perfecto(num):
        return {num}
    return otros_perfectos

f"""
print(numeros_perfectos([1,3,5,6,10]))
Esperado {6}
Se obtuvo {1, 6}
"""
def es_perfecto(num, divisor=2, acc=1):
    """Funcion auxiliadora que comprueba si el es perfecto

    Args:
        num (int): El numero a comprobar

    Returns:
        boolean : Devuelve TRUE o FALSE dependiendio si es divisor o no
    """
    if num == 1:
        return False
    if divisor > num/2:
        return num == acc
    if num % divisor == 0:
        return es_perfecto(num, divisor+1, acc+divisor)
    return es_perfecto(num, divisor+1, acc)

def numeros_perfectos(numeros, ind=0, perfectos=set()):
    """
    Función recursiva que itera sobre la lista de números y agrega
    a un conjunto aquellos que son perfectos utilizando la función
    "es_perfecto".

    Args:
        num (int): El numero a comprobar

    Returns:
    list : conjunto con los números perfectos encontrados.
    """
    if ind == len(numeros):
        return perfectos
    if es_perfecto(numeros[ind]):
        perfectos.add(numeros[ind])
    return numeros_perfectos(numeros, ind+1, perfectos)


def divisores(num):
    """Función auxiliar que devuelve una lista con todos los divisores propios del número

    Args:
        num (int): El numero a comprobar

    Returns:
        list : la lista con los divisores
    """
    lista_divisores = []
    for i in range(2, num):
        if num % i == 0:
            lista_divisores.append(i)
    return  lista_divisores

def numeros_perfectos(numeros):
    """Función recursiva que devuelve un conjunto con todos los números perfectos en una lista
    de números dada.

    Args:
        numeros (list): La lista con los numeros a comprobar

    Returns:
        set: Los numeros perfectos de la lista
    """
    # Comenzamos el set
    res = set()
    for num in numeros:
        # Calculamos los divisores
        suma_divisores = sum(divisores(num))
        # Comprobamos si es perfecto, si lo es no añadimos al set
        if num == suma_divisores:
            res.add(num)
    return res
