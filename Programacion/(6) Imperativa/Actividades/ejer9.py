x = int(input('Introduzca un numero: '))
Par_o_impar = lambda x: 'Si' if x % 2 == 0 else 'No'
print('Es Par?', Par_o_impar(x))
