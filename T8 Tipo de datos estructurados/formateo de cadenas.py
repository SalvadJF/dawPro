from math import pi

# Estas cadenas contienen campos de sustitución, que son expresiones encerradas entre llaves.
# En realidad, las cadenas formateadas son expresiones evaluadas en tiempo de ejecución.

ejemplo = f"El producto de 5 y 3 es {5 * 3}"

# La conversión !s llama a la función str sobre el resultado

ejemplo2 = f"El producto de 5 y 3 es {5 * 3!s}"

# se puede especificar formatos por x:? dice cuanto ancho deberia tener

x = 5
y = 3
print(f"El producto de 5 y 3 es {x:5} * {3}")

# en el caso de cadenas se añade el espacio por la derecha

nombre = 'Pepe'
print(f'El nombre es {nombre:20}')

# si quelemos cambiar la alineacion podemos usar <(izquierda)
# >(derecha) y ^(centro)

print(f'El nombre es {nombre:^20}')

# se puede especificar cuantos digitos quieres con 'presision' que es x:.?

print(f'El valor de pi es {pi:.4}')

# si usamos el :.?f especificamos cuantos decimales queremos

print(f'El valor de pi es {pi:.4f}')
