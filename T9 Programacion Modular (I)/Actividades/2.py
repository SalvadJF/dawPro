"""

Importa el módulo math en un programa que necesite la función math.gcd para calcular
el máximo común divisor de dos números:
a) Usando import math
b) Usando from math import gcd
c) Usando from math import *

¿Cuál es la diferencia entre las tres opciones? ¿Cuál es más conveniente? ¿Qué inconve-
nientes presenta la última opción?

"""

import math  as M
import gcd  from math
import *    from math

# a) Importa todo el módulo math, es comveniente si vamos  usar muchas funciones del módulo.
# b) Importa solo el gcd del modulo math, es util pues solo estamos sacando una unica funcion y gastando menos recursos.
# c) Importa todo del modulo math incluyendo las funciones ocultas. "__?__", no recomendado.
