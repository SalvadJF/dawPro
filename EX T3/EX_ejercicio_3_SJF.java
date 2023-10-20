/*
 * Escribe un programa que a partir de un array unidimensional:
 * a. Devuelva un array bidimensional (matriz cuadrada) cuya diagonal este formada por el array de entrada y el resto de elementos sea 0.
 * b. Muestre la matriz por pantalla, respetando la representacion convencional de matrices.
 * c. Calcule la suma de la diagonal de la matriz y muestee dicho valor por pantalla.
 */

 public class EX_ejercicio_3_SJF {
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
