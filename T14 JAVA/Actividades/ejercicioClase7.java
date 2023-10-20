
/*
 * Pide por teclado un intervalo entre 2 números. Luego imprime por pantalla todos los numeros enteros del intervalo diciendo los que son primos y los que no.
 */
import java.util.Scanner;

public class ejercicioClase7 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Ingrese el límite inferior del intervalo: ");
            int limiteInferior = sc.nextInt();

            System.out.print("Ingrese el límite superior del intervalo: ");
            int limiteSuperior = sc.nextInt();

            for (int i = limiteInferior; i <= limiteSuperior; i++) {
                boolean esPrimo = true;

                for (int j = 2; j < i; j++) {
                    if (i % j == 0) {
                        esPrimo = false;
                        break;
                    }
                }

                if (esPrimo) {
                    System.out.println(i + " es primo.");
                } else {
                    System.out.println(i);
                }
            }
        }
    }
}
