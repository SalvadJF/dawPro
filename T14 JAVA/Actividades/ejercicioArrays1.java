
/*
 *  Escribir un programa que solicite números al usuario y los vaya introduciendo en un
 *  array con una longitud inicial de 5. Si se supera la capacidad del array, se deberá ampliar
 *  usando la solución del ejercicio anterior. Cuando el usuario introduzca un 0, deberá
 *  mostrar todos los elementos almacenados en el array y finalizar el programa.
 */
import java.util.Scanner;

public class ejercicioArrays1 {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int[] numeros = new int[5];
            int contador = 0;
            while (true) {
                System.out.print("Introduzca un número: ");
                int numeroIngresado = scanner.nextInt();
                if (numeroIngresado == 0) {
                    break;
                }
                if (contador == numeros.length) {
                    int[] numerosNuevos = new int[numeros.length * 2];
                    for (int i = 0; i < numeros.length; i++) {
                        numerosNuevos[i] = numeros[i];
                    }
                    numeros = numerosNuevos;
                }
                numeros[contador++] = numeroIngresado;
            }
            System.out.println("Los números introducidos son:");
            for (int i = 0; i < contador; i++) {
                System.out.println(numeros[i]);
            }
        }
    }

}
