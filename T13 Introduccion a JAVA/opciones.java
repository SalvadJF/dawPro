import java.util.Scanner;

public class opciones {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean salir = false;
        String opcion;

        while (!salir) {

            System.out.println("1. Opción 1");
            System.out.println("2. Opción 2");
            System.out.println("3. Salir");


            System.out.print("Escribe una de las opciones: ");
            opcion = sc.next();

            switch (opcion) {
                case "1":
                    System.out.println("Seleccionaste la opción 1");
                    break;

                case "2":
                    System.out.println("Seleccionaste la opción 2");
                    break;

                case "3":
                    System.out.println("Saliendo del programa...");
                    salir = true;
                    break;

                default:
                    System.out.println("Solo números entre 1 y 3");
            }
        }
        System.out.println("Cerrando sc...");
        sc.close();
    }
}
