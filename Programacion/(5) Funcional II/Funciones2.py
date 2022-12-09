"""pre: n>0 digitos n=int post: digitos(n)= el numero de digitos de n"""

digitos = lambda n : 1 if n <= 10 else 1 + digitos (n/10)

"""       {Pre:  1 si n < 10                  (caso base)
  digitos {
          {Post: 1 + digitos(n/10) si n > 10  (caso recursivo)
"""
"""5. La función suma_digitos calcula la suma de los dígitos de un número entero:
Se pide:
a) Escribir su especificación.
b) Implementar una función recursiva que satisfaga dicha especificación.
Indicación: Recordar que n // 10 le quita el último dígito a 𝑛. Además, n % 10 devuelve
el último dígito de 𝑛.

            {Pre:  True
suma_digitos{    suma_digitos(n:int)->int
            {Post: suma_digitos(n)=la suma de los digitos de n ^ suma_digitos(n)>=0
"""

Asuma_digitos = lambda n : abs(n) if abs(n) < 10 else abs(n) % 10 + Asuma_digitos(abs(n) // 10)

"""parametros acumuladores"""
suma_iter = lambda n, acc : acc if n == 0 else suma_iter((n//10),(acc + n % 10))

suma_digitos = lambda n : suma_iter(n,0)

"""convertir a iterativa"""
invertir = lambda s : "" if s == "" else invertir(s[1:]) + s[0]

invertir_iter = lambda s, acc : acc if s == "" else invertir_iter (s[1:], s[0] + acc)

"""
Pre {                                                           | 0 , a > b (caso base)
    { suma(a:int,b:int) -> int                                  |
Post{ suma(a,b)=la suma de los enteros comprendidos entre a y b | a + suma(a +1,b)
"""
Asumacon = lambda a, b : 0 if a > b else a + Asumacon(a + 1, b)

sumacon_iter = lambda a, b, acc :acc if a > b else sumacon_iter (a + 1, b , acc + a)

sumacon = lambda a, b : sumacon_iter(a , b, 0)
