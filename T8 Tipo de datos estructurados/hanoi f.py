#hanoi con formateo de candenas

def hanoi(a, b , c ,n):
    if n == 0:
        return
    hanoi(a, b, c, n - 1)
    print(f'mueve un disco de {a} a {b}')
    hanoi(c, b, a, n - 1)

print(hanoi('a', 'b', 'c', 5))
