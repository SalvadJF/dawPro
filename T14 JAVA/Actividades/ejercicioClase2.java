
/*
 *  Introduce tu nombre por pantalla, después muestra un mensaje de bienvenida por consola.
 *
 *  Por ejemplo: si introduzco «Fernando», me aparezca «Bienvenido Fernando».
 */
import java.util.Scanner;

public class ejercicioClase2 {

    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Introduce tu nombre: ");
            String nombre = scanner.next();

            System.out.println("Bienvenido " + nombre);
        }
    }
}
