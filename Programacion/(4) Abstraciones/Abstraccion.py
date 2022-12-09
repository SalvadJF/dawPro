"""2. Escribir una función que implemente la siguiente especificación"""

from cmath import sqrt


repite = lambda s , n : s * n

"""3. Escribir una función que implemente la siguiente especificación:"""

es_vocal = lambda x : x == "a" or x == "e" or x == "i" or x == "u" or x == "o"

"""4. Escribir una función calculadora a la que se le pasan dos números reales y qué ope-
ración se desea realizar con ellos. Las operaciones disponibles son: sumar, restar, mul-
tiplicar o dividir. Éstas se especifican mediante un carácter: '+', '-', '*' o '/', res-
pectivamente. La función devolverá el resultado de la operación en forma de número
rea"""

calculadora_suma = lambda x , y : x + y
calculadora_resta = lambda x , y : x - y
calculadora_multi = lambda x , y : x * y
calculadora_divi = lambda x , y : x / y

"""5. Escribir una función que calcule la distancia euclídea entre dos puntos (𝑥1, 𝑦1) y (𝑥2, 𝑦2),
descrita por la siguiente especificación:"""

distancia = lambda x , y , a , b :sqrt(((x - a)**2)+((y - b)**2))

"""6. Escribir una función que reciba una cantidad de días, minutos y segundos, y que calcule
y devuelva el número de segundos en los datos de entrada indicados. Dar un ejemplo
de uso."""

tiempo = lambda x , y , z : ((x * 86400) + (y + 60) + z)

"""7. Escribir una función que reciba dos instantes de tiempo en forma de horas y minutos y
que cumpla con la siguiente especificación:"""

diferenciaT = lambda x , y , z , a :((x * 60)+y) - ((z * 60)+ a)
