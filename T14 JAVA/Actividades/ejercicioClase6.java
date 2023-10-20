
/*
 * Pide 5 números por teclado, los suma y los guarda en un array, luego imprime por pantalla la suma y los números en orden inverso.
 */

import java.util.Scanner;

public class ejercicioClase6 {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int[] nums = new int[5];
            int sum = 0;
            for (int i = 0; i < nums.length; i++) {
                System.out.print("Ingrese el número " + (i+1) + ": ");
                nums[i] = scanner.nextInt();
                sum += nums[i];
            }
            System.out.println("Suma de los números: " + sum);
            System.out.print("Números en orden inverso: ");
            for (int i = nums.length-1; i >= 0; i--) {
                System.out.print(nums[i] + " ");
            }
        }
    }
}
