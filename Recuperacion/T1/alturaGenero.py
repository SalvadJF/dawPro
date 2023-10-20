"""
Los médicos forenses utilizan la longitud de ciertos
huesos para determinar la altura de una persona, cuando la persona estaba viva.

     Para varones:

- Altura (en cm)= 69.089 + 2.238 * longitud_de_la_tibia


     Para mujeres:

- Altura (en cm)= 61.412 + 2.317 * longitud_de_la_tibia

Escribir en Python una función llamada "altura_genero()" que,
teniendo en cuenta lo comentado anteriormente, calcule altura de cada individuo,
adquiriendo los datos de un archivo (llamado: registro.txt), para ello, el formato
del archivo ha de ser como sigue (esto es un ejemplo,
para sacar el formato, utilizar el archivo "registro.txt"):


Al invocar a la función "altura_genero()", se debe obtener como resultado otro archivo
de salida llamado "alturas.txt". Además, cada altura calculada se ha de truncar para que
no tengan parte decimal. Debiéndose obtener, un archivo como el que sigue:



Indicación: se pueden usar campos de sustitución en una
f-string con el formato {numero:anchof} para alinear un número entero a la derecha.
Por ejemplo:
>>> f'{25:9}'
'       25'

Observación: Antes de comprobar los tests, se hace lo siguiente:

altura_genero()
altura = [x.rstrip() for x in open('alturas.txt').readlines()]



Por ejemplo:
Test 	Resultado

print("'" + altura[2][26:] + "'") = '136'


"""

"""
Archivos a usar
registro.txt
Genero L_Tibia[cm]
------ -----------
  H             30
  M             27
  M             31
  H             50

Archivo resultado

alturas.txt
Genero L_Tibia[cm] Altura[cm]
------ ----------- ----------
  H             30        136
  M             27        123
  M             31        133
  H             50        180


"""
""" SJF """
def altura_genero():
    """Funcion lee los archivos y calcula la altura de cada individuo segun su genero

    Args:
        Archivos registro,txt y alturas.txt

    Returns:
        Escribe en el archivo alturas los nuevos individuos
    """
    with open('registro.txt', 'r',encoding='utf-8') as archivo_entrada:
        # Leer todas las líneas del archivo, excepto la primera
        lineas = archivo_entrada.readlines()[1:]

    # Abrir el archivo de salida para escribir las alturas calculadas
    with open('alturas.txt', 'w',encoding='utf-8') as archivo_salida:
        # Escribir las cabeceras en el archivo de salida
        archivo_salida.write('{:<8} {:<14} {:<10}\n'.format('Genero', 'L_Tibia[cm]', 'Altura[cm]'))
        archivo_salida.write('{:<8} {:<14} {:<10}\n'.format('------', '-----------', '----------'))

        # Calcular la altura para cada línea del archivo de entrada
        for linea in lineas:
            # Dividir la línea en género y longitud de la tibia
            genero, longitud_tibia = linea.split()

            # Remove the 'cm' from the length of tibia
            longitud_tibia = longitud_tibia.rstrip('cm')

            # Calcular la altura según el género
            if genero == 'H':
                altura = int(69.089 + 2.238 * float(longitud_tibia))
            else:
                altura = int(61.412 + 2.317 * float(longitud_tibia))

            # Escribir la altura calculada en el archivo de salida
            archivo_salida.write('{:<8} {:<14} {:<10}\n'.format\
              (genero, longitud_tibia+'cm', altura))
