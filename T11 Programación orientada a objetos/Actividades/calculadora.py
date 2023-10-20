class Calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.opcion = 0

    def pedir_datos(self):
        self.opcion = int(input("\n¿Qué operación deseas realizar? \
            \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Salir \n "))
        if self.opcion in range(1, 5):
            self.num1 = int(input("Introduce el primer número: "))
            self.num2 = int(input("Introduce el segundo número: "))
    def calcular(self):
        while True:
            if self.opcion == 1:
                resultado = self.num1 + self.num2
                print("\n El resultado de la suma es:", resultado)
            elif self.opcion == 2:
                resultado = self.num1 - self.num2
                print("\n El resultado de la resta es:", resultado)
            elif self.opcion == 3:
                resultado = self.num1 * self.num2
                print("\n El resultado de la multiplicación es:", resultado)
            elif self.opcion == 4:
                if self.num1 == 0 or self.num2 == 0:
                    print("\n No se puede dividir por 0")
                else:
                    resultado = self.num1 / self.num2
                    print("\n El resultado de la división es:", resultado)
            elif self.opcion == 5:
                print("\n ¡Hasta Luego!")
                break
            else:
                print("\n Opción no válida")
            self.pedir_datos()

calculadora = Calculadora()
calculadora.pedir_datos()
calculadora.calcular()
