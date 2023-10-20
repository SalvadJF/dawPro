
/*
 * Crea un programa que simule un sistema de permisos para una aplicación y te permita verificar si un usuario tiene ciertos permisos especificos.
 * Cada permiso se representa mediante un número entero y un usuario puede tener varios permisos.
 *
 * Haz el programa anterior más eficiente. No utilices ningún tipo de bucle. PISTA:  Utiliza operadores binarios
 */

 public class ejercicioClase10 {
    public static final int PERMISO_A = 1 << 0; // Permiso 1
    public static final int PERMISO_B = 1 << 1; // Permiso 2
    public static final int PERMISO_C = 1 << 2; // Permiso 3
    public static final int PERMISO_D = 1 << 3; // Permiso 4
    // Agregar los permisos necesarios

    public static void main(String[] args) {
        int permisosUsuario1 = PERMISO_A | PERMISO_C; // Usuario 1 tiene permiso A y C
        int permisosUsuario2 = PERMISO_B | PERMISO_D; // Usuario 2 tiene permiso B y D
        // Definir los permisos de los demás usuarios

        boolean tienePermisoA = (permisosUsuario1 & PERMISO_A) != 0; // True si el usuario 1 tiene permiso A
        boolean tienePermisoB = (permisosUsuario2 & PERMISO_B) != 0; // True si el usuario 2 tiene permiso B
        // Verificar los permisos de los demás usuarios

        System.out.println("El usuario 1 tiene permiso A: " + tienePermisoA);
        System.out.println("El usuario 2 tiene permiso B: " + tienePermisoB);
        // Imprimir los permisos de los demás usuarios
    }
}
