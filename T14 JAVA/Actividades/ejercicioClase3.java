
/*
 *  Lee un número por teclado y muestra por consola, el carácter al que pertenece en la tabla ASCII. Por ejemplo: si introduzco un 97, me muestre una a.
 *  Modifica el ejercicio anterior, para que en lugar de pedir un número, pida un carácter (char) y muestre su código en la tabla ASCII.
*/

import java.util.Scanner;

public class ejercicioClase3 {
  public static void main(String[] args) {
    try (Scanner sc = new Scanner(System.in)) {
        System.out.print("Ingresa un número o una letra: ");
        String input = sc.next();

        char caracter = input.charAt(0);

        int ascii = (int) caracter;

        System.out.println("El carácter " + caracter + " en código ASCII es: " + ascii);
    }
  }
}
