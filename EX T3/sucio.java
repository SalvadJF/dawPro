/*
public class sucio {
    public static void main(String[] args) {
        // Definimos el array de entrada
        int[] ejemploArray = {1, 2, 3, 4, 5};

        // Creamos la matriz cuadrada
        int[][] matriz = new int[ejemploArray.length][ejemploArray.length];

        // Asignamos los valores al array
        for (int i = 0; i < ejemploArray.length; i++) {
            matriz[i][i] = ejemploArray[i];
        }

        // Calculamos la suma de la diagonal
        int diagonalSum = 0;
        for (int i = 0; i < ejemploArray.length; i++) {
            diagonalSum += matriz[i][i];
        }

        // Mostramos la matriz y la suma por pantalla
        System.out.println("Matriz resultante:");
        for (int i = 0; i < ejemploArray.length; i++) {
            for (int j = 0; j < ejemploArray.length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("La suma de la diagonal es: " + diagonalSum);
    }
}
*/



public class sucio {

    public static void main(String[] args) {
        // El array que vamos a usar para el ejemplo
        int[] entrada = {1, 3, 5, 10, 15, 27, 200, 630 , 2000};
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
            // Al terminar el bucle for cerramos
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
