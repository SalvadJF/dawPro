#Dibujar un triangulo

t = [[1],[1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

def dibujar_triangulo(t):
    for fila in t:
        res = []
        for e in fila:
            res.append(f"{e:4}")
        res = ' '.join(res)
        print(f'{res:^30}')

dibujar_triangulo(t)
