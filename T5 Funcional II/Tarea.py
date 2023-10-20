"""
base

rota(n,()) = ()
rota(0,t) = t

recursivo
rota(n,t) =
insertar(rota(n-1, t[1:])), t[0], len(t) - n)
"""
"""
Pre: 0 <= p < lent(t)

base
insertar((), x, p) = (x,)
insertar(t, x, 0) = (x,) + t

insertar (t,x,p) = (t[0],) + insertar (t[1:], x, p -1)

rota = lambda n, t: () if t == () else t if n == 0 else \
     insertar(rota(n - 1, t[1:]), t[0], len(t) - n)

"""
insertar = lambda t, x, p: (x,) if t == () else (x,) + t if p == 0 else \
     (t[0],) + insertar(t[1:], x, p - 1)

rota = lambda n , t: t if n == 0 else rota((n - 1), t[1:] + (t[0],))

rotar_iter = lambda n, t: t if n == 0 else rotar_iter(n - 1 , t[1:] + (t[0],))

"""
concatenar tuplas
casos bases
() + t2 = t2
(t,) + t2 = (t, t2, ....)
"""

concatenar = lambda t1, t2: t2 if t1 == () else t1 + t2 if len(t1) == 1 else \
    (t1[0],) + concatenar(t1[1:], t2)

"""
menor y mayor

          base  t[0] si len(t) == 1
menor (t)
          min(t[0], menor(t[1:]))

          base  t[0] si len(t) == 1
mayor (t)
          max(t[0], mayor(t[1:]))
"""
"""
menor = lambda t: t if len(t) == 1 else min(t[0], menor[t[1:]])

mayor = lambda t: t if len(t) == 1 else max(t[0], mayor[t[1:]])

"""
menor_aux = lambda t, acc: acc if t == 0 else menor_aux(t[1:], min(t[0], acc))
menor = lambda t: menor_aux(t, t[0])

menor_mayor = lambda t, me, ma : (me, ma) if t == () else menor_aux(t[1:], min(t[0]), me), max(t[0], ma))
