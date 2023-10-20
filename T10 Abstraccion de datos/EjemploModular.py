# Módulo de suma
def suma(num1, num2):
    return num1 + num2

# Módulo de resta
def resta(num1, num2):
    return num1 - num2

# Módulo de multiplicación
def multiplicacion(num1, num2):
    return num1 * num2

# Módulo de división
def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir entre cero"
    return num1 / num2

# Programa principal
while True:
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Ingrese una opción (1-5): "))
    if opcion not in (1, 2, 3, 4, 5):
        print("")
        print("Opción no válida")
        print("")
        continue
    if opcion == 5:
        print("                ")
        print("¡Hasta luego!")
        print("")
        break
    print("")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        resultado = suma(num1, num2)
        print("")
        print("El resultado de la suma es:", resultado)
        print("")
    elif opcion == 2:
        resultado = resta(num1, num2)
        print("")
        print("El resultado de la resta es:", resultado)
        print("")
    elif opcion == 3:
        resultado = multiplicacion(num1, num2)
        print("")
        print("El resultado de la multiplicación es:", resultado)
        print("")
    elif opcion == 4:
        resultado = division(num1, num2)
        print("")
        print("El resultado de la división es:", resultado)
        print("")
