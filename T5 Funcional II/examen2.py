
qd_iter = lambda s, acc: acc if s == '' \
        else qd_iter(s[1:], acc + ('' if s[0].isdigit() else s[0]))

quitar_digitos = lambda s: qd_iter(s, '')
#tomar_mientras
tm = lambda f, t: () if t == () \
    else t[0] + tm(f, t[1:])
