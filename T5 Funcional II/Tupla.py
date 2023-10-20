"""
   |() caso base
t =|
   |(t[0],) + t[1:]
"""
"""
                |Pre: todos los elementos de la tupla son int
Caso recursivo  |     suma_t(t:tuple[int]) -> int
                |Post:suma_t = a la suma de los elementos de t
"""
Asuma_t = lambda t : 0 if t == () else t[0] + Asuma_t(t[1:])

suma_iter = lambda t, acc : acc if t == () else suma_iter(t[1:], acc + t[0])

suma_t = lambda t :suma_iter(t, 0)

"""

media [precondicion t != () ]

"""

media_iter = lambda t, acc, cont : acc / cont if t == () else media_iter(t[1:], acc + t[0], cont + 1)
media = lambda t : media_iter(t, 0, 0)

"""

longitud de tupla

"""
Alongitud = lambda t : 0 if t == () else 1 + Alongitud(t[1:])
long_iter = lambda t, cont : cont if t == () else long_iter(t[1:], cont + 1)
longitud = lambda t : long_iter(t, 0)

Imedia = lambda t: suma_t(t)/longitud(t)

esta_aprobado = lambda t : media(t) >= 4.5

"""
       |
lista =|(("AP,(1,4,7)),(MR(8,7,5)),(SG(9,10)))
       |
"""
antonio = ("AP",(1., 4., 7.))
maria = ("MR", (8., 7., 5.))
sonia = ("SG", (9.,10.))
matriculas = (antonio, maria, sonia)
"""
snd = lambda t : t[1:][0]
"""
nombre = lambda t : t[0]
notas = lambda t : t[1:][0]
"""
pre: todos los elemntos de t tienen que cumplir que t[1:][0] no puede ser igual a ()
aprobados(m: tuple[tuple[str, tuple[float]]]) -> tuple[str]
post aprobados(m)=la tupla que contiene los nombres de los aprobados
"""
Aaprobados = lambda m : () if m == () else esta_aprobado(m[0][1:][0])

aprobados = lambda m : () if m == () else (nombre(m[0]) + aprobados(m[1:])) if esta_aprobado(notas(m[0])) else () + aprobados (m[1:])
