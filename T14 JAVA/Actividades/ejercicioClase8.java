
/*
 * Crea el juego de piedra, papel o tijeras.
 * En una primera versión, la respuesta del jugador 1 y del jugador 2 se introduce por el teclado:P -> piedraL -> papelT -> tijerasEn la segunda versión,
 * la respuesta del jugador 2 se calcula de manera aleatoria.
 */
import java.util.Scanner;
import java.util.Random;

public class ejercicioClase8 {

    public static void main(String[] args) {

        try (Scanner sc = new Scanner(System.in)) {
            Random random = new Random();
            String eleccionJugador1, eleccionJugador2;

            System.out.println("¡Bienvenido al juego de Piedra-Papel-Tijera!");
            System.out.println("Jugador 1, por favor ingrese su elección (P para piedra, L para papel, T para tijera):");
            eleccionJugador1 = sc.next().toUpperCase();

            // Asegúrate de que el Jugador 1 haya ingresado una opción válida
            while (!(eleccionJugador1.equals("P") || eleccionJugador1.equals("L") || eleccionJugador1.equals("T"))) {
                System.out.println("Por favor ingrese una opción válida (P para piedra, L para papel, T para tijera):");
                eleccionJugador1 = sc.next().toUpperCase();
            }

            // Genera una elección aleatoria para el Jugador 2
            int numeroAleatorio = random.nextInt(3); // genera un entero aleatorio entre 0 y 2
            switch (numeroAleatorio) {
                case 0:
                    eleccionJugador2 = "P"; // piedra
                    break;
                case 1:
                    eleccionJugador2 = "L"; // papel
                    break;
                case 2:
                    eleccionJugador2 = "T"; // tijera
                    break;
                default:
                    eleccionJugador2 = ""; // no debería llegar a este punto
                    break;
            }
            System.out.println("La elección del Jugador 2 es: " + eleccionJugador2);

            // Determina el ganador
            if (eleccionJugador1.equals(eleccionJugador2)) {
                System.out.println("¡Es un empate!");
                main(args); //Inicia el programa nuevamente si hay un empate
            } else if (eleccionJugador1.equals("P") && eleccionJugador2.equals("T") ||
                       eleccionJugador1.equals("L") && eleccionJugador2.equals("P") ||
                       eleccionJugador1.equals("T") && eleccionJugador2.equals("L")) {
                System.out.println("¡Jugador 1 gana!");
            } else {
                System.out.println("¡Jugador 2 gana!");
            }
        }

    }

}
