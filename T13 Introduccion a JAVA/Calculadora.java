import java.util.Scanner;

public class Calculadora {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            String opcion;

            while (true) {
                System.out.println("\nElija la operación a realizar:");
                System.out.println("1) Suma");
                System.out.println("2) Resta");
                System.out.println("3) Multiplicación");
                System.out.println("4) División");
                System.out.println("5) División entera");
                System.out.println("6) Módulo");
                System.out.println("7) Potencia");
                System.out.println("8) Puerta AND a nivel de bit");
                System.out.println("9) Puerta OR a nivel de bit");
                System.out.println("10) Salir");

                opcion = scanner.next();

                if(opcion.equals("10")) {
                    System.out.println("¡Hasta luego!");
                    return;
                }

                System.out.print("Ingrese el primer número: ");
                double num1 = scanner.nextDouble();
                System.out.print("Ingrese el segundo número: ");
                double num2 = scanner.nextDouble();

                double resultado = 0;

                switch(opcion) {
                    case "1":
                        resultado = num1 + num2;
                        break;
                    case "2":
                        resultado = num1 - num2;
                        break;
                    case "3":
                        resultado = num1 * num2;
                        break;
                    case "4":
                        if(num1 == 0 || num2 == 0) {
                            System.out.println("Error: no se puede dividir entre cero.");
                        } else {
                            resultado = num1 / num2;
                        }
                        break;
                    case "5":
                        if(num1 == 0 || num2 == 0) {
                            System.out.println("Error: no se puede dividir entre cero.");
                        } else {
                            resultado = (int) (num1 / num2);
                        }
                        break;
                    case "6":
                        resultado = num1 % num2;
                        break;
                    case "7":
                        resultado = Math.pow(num1, num2);
                        break;
                    case "8":
                        resultado = (byte) num1 & (byte) num2;
                        break;
                    case "9":
                        resultado = (byte) num1 | (byte) num2;
                        break;
                    default:
                        System.out.println("Opción inválida.");
                        continue; // repetir el ciclo
                }

                System.out.println("El resultado es: " + resultado);
            }
        }
    }
}
