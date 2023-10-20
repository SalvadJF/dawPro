/*
 * Escribe un programa que reciba un array de numeros enteros y devuelva otro array formado por los enteros
 * que cumplen la propiedad, ser numeros triangulares.
 * Imprime por pantalla dicho array.
 * Si ninguno de los elementos del array es un numero triangular devuelve el siguiente mensaje "El array de entrada no contiene numeros triangulares"
 *
 * Validacion:
 * Entrada = [1,3,5,10,15]
 * Salida = "Los numeros triangulares son [3,10,15]"
 */

 public class EX_ejercicio_1_SJF {

    public static void main(String[] args) {
        // El array que vamos a usar para el ejemplo
        int[] entrada = {1, 3, 5, 10, 15};
        // Contamos la cantidad de objetos en el array
        int[] resultados = new int[entrada.length];
        int contador = 0;

        for (int i = 0; i < entrada.length; i++) {
            // Se pasa los objetos del array por la funcien es triangular
            if (esTriangular(entrada[i])) {
                resultados[contador] = entrada[i];
                contador++;
            }
        }

        if (contador == 0) {
            // Salta si el array no contiene numeros triangulares
            System.out.println("El array de entrada no contiene numeros triangulares");
        } else {
            // Imprime los numeros triangulares contenidos en la variable
            System.out.print("Los numeros triangulares son [");
            for (int i = 0; i < contador-1; i++) {
                System.out.print(resultados[i] + ",");
            }
            // Al terminar el bucle for, cerramos
            System.out.println(resultados[contador-1] + "]");
        }
    }

    public static boolean esTriangular(int n) {
        /*
         * Esta funcion comprobara si el numero es un numero triangular
         * Un numero triangular es aquel es un numero que se obtiene al sumar numeros naturales consecutivos
         * EJ 15 = 1 + 2 + 3 + 4 + 5 Por tanto es triangular
         * EJ  5 No puede ser triangular pues no puede expresarse de esa forma
         */
        int suma = 0;
        int i = 1;
        /*
         *   Este if existe en caso del que numero sea uno 1, para que no se reconozca como numero Triangular.
         *   pues el siguiente bucle lo daria por valido pese que en la teoria 1 no es triangular
         */
        if (n == 1){
            return false;
        }
        else{
            while (suma < n) {
                suma += i;
                i++;
            }
            return suma == n;
        }
    }
}
