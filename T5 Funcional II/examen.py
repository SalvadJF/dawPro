"""quitar_digitos_iter = lambda a, acc, t: t if a == "" else quitar_digitos_iter(a[1:], (acc + (a[0])) + t)
if (a[0] == int) else quitar_digitos_iter(a[1:]) + acc + (t + (a[0]))

quitar_digitos = lambda a: quitar_digitos_iter(a, 0, 0)"""



"""quitar = lambda a, acc: acc if a == ("") else quitar(a[1:] +\
(acc + a[0:])) if a[0] == str else quitar[1:] + acc

quitar_digitos = lambda a: quitar(a, 0)"""


quitar_digitos_nor = lambda s: "".join(filter(lambda x: not x.isdigit(), s))
quitar_digitos_gen = lambda s: "".join(s for () in s if not s.isdigit())
tomar_mientras = lambda f , t: () if t == () else ()  \
    if not f(f(0)) else (t[0],) + tomar_mientras(f, t[1:])
quitar_mientras = lambda f , t: () if t == () else t  \
    if not f(f(0)) else (t[0],) + quitar_mientras(f, t[1:])
dejar_mientras = lambda f , t: () if t == () else t if not f(t(0)) else dejar_mientras(f, t[1:])
