/*
 * Crear un método rellenaCuadrado que reciba un entero 𝑛 y que devuelva una matriz
 * Cuadrada de 𝑛 × 𝑛 que sólo contenga al entero 𝑛.
 */

import java.util.Arrays;

public class ejercicioArrays3 {
    public static int[][] rellenaCuadrado(int n) {
        int[][] matriz = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(matriz[i], n);
        }

        return matriz;
    }

    public static void main(String[] args) {
        int[][] miMatrix = ejercicioArrays3.rellenaCuadrado(3); // Crea un cuadrado 3x3

        for(int[] cuadrado : miMatrix) {
            System.out.println(Arrays.toString(cuadrado));
        }
    }
}
