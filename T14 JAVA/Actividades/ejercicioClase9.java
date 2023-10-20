/*
 * Crea un programa que pida un número por teclado, y devuelva por pantalla un mensaje indicando si el numero introducido es una potencia de 2.
 *
 * Haz el programa anterior más eficiente. No utilices ningún tipo de bucle. PISTA:  Utiliza operadores binarios
 */

import java.util.Scanner;

public class ejercicioClase9 {

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Introduce un número: ");
            int number = sc.nextInt();
            if ((number & (number - 1)) == 0) { /*
                                                 * El operador & combierte ambos numeros que compara en binario
                                                 * EJ: 4 en binario es 100, 4-1 = 3, 3 en binario es 011, al no coincidir ningun bit el resultado es 000 = 0
                                                 * Por tanto es potencia de 2
                                                */
                System.out.println(number + " es una potencia de 2");
            } else {
                System.out.println(number + " no es una potencia de 2");
            }
        }
    }

}
