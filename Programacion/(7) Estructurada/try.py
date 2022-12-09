try:
    x = int(input("Introduzca un número entero: "))
    print(x * 3)
except ValueError:
    print("¡Vaya! No ha introducido un número entero.")
else:
    print("La cosa ha acabado bien.")
finally:
    print("Fin")
