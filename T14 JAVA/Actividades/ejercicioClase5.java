
/*
 * Escribe una aplicación con un String que contenga una contraseña cualquiera. Después se te pedirá que introduzcas la contraseña, con 3 intentos.
 * Cuando aciertes ya no pedirá mas la contraseña y mostrara un mensaje diciendo «Enhorabuena».
 * Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden intentos)
 */

import java.util.Scanner;
public class ejercicioClase5 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String password = "contraseña"; // definimos la contraseña
            int intentos = 0;
            boolean acertado = false;
            do {
                System.out.print("Introduce la contraseña: ");
                String entrada = sc.nextLine();
                intentos++;
                if (entrada.equals(password)) { // si la contraseña es correcta
                    System.out.println("Enhorabuena, has acertado!");
                    acertado = true;
                } else { // si la contraseña es incorrecta
                    System.out.println("Contraseña incorrecta.");
                }
            } while (intentos < 3 && !acertado); // se repite mientras haya intentos y no se haya acertado
        }
    }
}
