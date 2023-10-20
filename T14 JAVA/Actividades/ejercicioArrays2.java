
/*
 * Escribe un programa que represente la matriz
 *  1 2 3
 *  4 5 6
 *  7 8 9
 *  usando un array bidimensional inicializando a los valores adecuados. A continuación muestra los valores de la matriz usando dos bucles anidados
 *
*/

public class ejercicioArrays2 {
    public static void main(String[] args) {
        int[][] matriz = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

        for(int i = 0; i < matriz.length; i++){
            for(int j = 0; j < matriz[i].length; j++){
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
