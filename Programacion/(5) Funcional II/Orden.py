from functools import reduce


"""divisores = lambda n : reduce(lambda a , e: a + int(n % e == 0), range(1, n + 1), 0)"""
divisores = lambda n : sum(1 for i in range(1, n + 1) if n % i == 0)

es_primo = lambda n : divisores(n) == 2

suma_cuad_primos_menor = lambda n : (i ** 2 for i in range(1, n) if es_primo(i))

tupla_primos_menor = lambda n : tuple(i for i in range(1, n) if es_primo(i))

dado = tuple((x,y) for x in range(1, 7) for y in range(1, 7) if x + y == 7)

"""

                 |caso base:      si n=0
hanoi(a, b ,c, n)|
                 |caso recursivo: (a,c,b,n-1) + ("muevo de "+str(a) + "a" + str(b))

"""


hanoi  = lambda a, b, c, n : () if n == 0 else hanoi(a, c ,b, n - 1)\
+ ("muevo 1 disco de " + str(a) + "a" + str(b),) + hanoi(c, b, a, n -1)
