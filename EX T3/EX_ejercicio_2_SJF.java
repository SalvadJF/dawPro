/*
 * Escribe un programa que devuelva por pantalla el numero de palabras de una cadena de texto.
 * Los signos de puntuacion no se tendran en cuenta.
 *
 * Entrada = Si buscas resultados distintos, no hagas siempre lo mismo
 * Salida = "El texto esta formado por 9 palabras"
 */

public class EX_ejercicio_2_SJF {

    public static void main(String[] args) {
    // La cadena de texto a analizar como ejemplo
    String texto = "Si buscas resultados distintos, no hagas siempre lo mismo";

    // Eliminamos cualquier signo de puntuación que aparezca en la cadena de texto
    // Para ello usaremos la siguiente expresion regular
    texto = texto.replaceAll("[^a-zA-Z0-9 ]", "");

    // Separamos la cadena de texto en palabras individuales utilizando un separador (en este caso, un espacio en blanco)
    String[] palabras = texto.split(" ");

    // Contamos el número de palabras resultantes
    int numPalabras = palabras.length;

    // Mostramos el resultado por pantalla
    System.out.println("El texto está formado por " + numPalabras + " palabras.");
    }
 }
