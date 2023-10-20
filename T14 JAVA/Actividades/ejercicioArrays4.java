
/*
 *  Crear un programa que cree un array de cinco elementos, donde el primero sea un
 *  entero, el segundo una cadena, el tercero un booleano, el cuarto un valor null y el quinto
 *  un StringBuilder. Luego debe enviar ese array a un método estático que recorrerá el
 *  array desde el primer elemento hasta el último y los mostrará por la salida.
 */

public class ejercicioArrays4 {
    public static void main(String[] args) {
        Object[] miArray = { 5, "Hola", true, null, new StringBuilder()};
        mostrarArray(miArray);
    }

    public static void mostrarArray(Object[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
    }
}
