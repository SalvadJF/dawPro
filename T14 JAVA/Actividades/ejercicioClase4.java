import java.util.Scanner;

/*
 * Realiza una aplicacion que nos calcule una ecuacion de segundo grado.
 * Debes pedir las variables a, b y c por teclado y comprobar antes que el discriminate(operacion en la raiz cuadrada).
 * Para la raiz cuadrada usa el metodo sqlrt de Math
*/
public class ejercicioClase4 {
   public static void main(String[] args) {
      try (Scanner sc = new Scanner(System.in)) {
        double a, b, c, discriminante, x1, x2;

          System.out.println("Este programa calcula las soluciones de una ecuación de segundo grado.");
          System.out.print("Introduce el valor de a: ");
          a = sc.nextDouble();

          System.out.print("Introduce el valor de b: ");
          b = sc.nextDouble();

          System.out.print("Introduce el valor de c: ");
          c = sc.nextDouble();

          discriminante = (b * b) - 4 * (a * c);

          if (discriminante < 0) {
             System.out.println("Esta ecuación no tiene soluciones reales.");
          } else {
             x1 = (-b + Math.sqrt(discriminante)) / (2 * a);
             x2 = (-b - Math.sqrt(discriminante)) / (2 * a);

             System.out.println("Las soluciones de la ecuación son:");
             System.out.println("x1 = " + x1);
             System.out.println("x2 = " + x2);
          }
    }
   }
}
