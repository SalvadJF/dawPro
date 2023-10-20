/*
 * Escribir un programa que a partir de un archivo de texto  llamado mis_empleados.txt.  y tiene la siguiente estructura:
 * InicialesNombreApellidosEmpleado_Sexo_Edad_NivelEmpresa
 * MLR_M_31_8,RPL_H_47_15,TLG_M_28_6,JGL_H_35_9,STF_H_27_8,GRP_H_40_13,
 * FLG_H_20_0,MSH_M_23_0,RLR_H_34_10,APR_H_27_6,MNR_M_33_9,TAJ_M_31_15
 *
 * Se pide:
 * - Almacenar en un array unidimensional de tipo String la información del fichero que viene delimitada por ",".
 * - Transformar dicho array en una matriz de tipo Objeto donde para cada empleado se almacena en distintas columnas sus iniciales (String), sexo(String), edad (Int) y nivel(Int)
 * Ej: {{MLR, M, 31, 8}, {APR, H, 54, 14}}.
 * - Define un método estático dentro de la clase principal que permita filtrar la matriz por alguno de sus campos.
 * - Define un método estático dentro de la clase principal para calcular la edad media de un conjunto de empleados. El parametro de entrada será un array bidimensional con los empleados requeridos.
 * - Define un método estático que defina la promoción de un empleado. Si un empleado es promocionado, entonces su nivel aumenta en 1. Ojo! Si tiene el nivel máximo no puede promocionar más.
 * - Una vez definido los métodos, muestra por pantalla, los empleados que son mujeres, calcula su edad media y promociónalas.
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ejercicioArrays5 {

    public static void main(String[] args) {
        String[] empleadosArray = obtenerEmpleadosDesdeArchivo("mis_empleados.txt");
        Object[][] empleadosMatriz = transformarEmpleadosAHojas(empleadosArray);
        // Filtrar la matriz por algún campo (en este caso se filtra por sexo)
        Object[][] empleadosFiltrados = filtrarEmpleadosPorCampo(empleadosMatriz, 1, "M");
        // Calcular la edad media de los empleados filtrados previamente
        double edadMedia = calcularEdadMedia(empleadosFiltrados);
        // Promocionar a todos los empleados filtrados previamente
        promocionarEmpleados(empleadosFiltrados);

        // Imprimir en consola los empleados mujeres, su edad media y la matriz después de ser promocionada
        System.out.println("Empleados Mujeres: ");
        imprimirEmpleados(empleadosFiltrados);
        System.out.println("Edad Media: " + edadMedia);
        System.out.println("Matriz Después de ser Promocionada: ");
        imprimirEmpleados(empleadosMatriz);
    }

    /**
     * Método para obtener el contenido del archivo de empleados y almacenarlo en un array.
     *
     * @param nombreArchivo El nombre del archivo a leer.
     * @return Un array con la información de cada empleado.
     */
    public static String[] obtenerEmpleadosDesdeArchivo(String nombreArchivo) {
        String[] empleadosArray = null;

        try {
            File archivo = new File(nombreArchivo);
            try (Scanner sc = new Scanner(archivo)) {
                sc.useDelimiter(",");

                String empleadosString = sc.next();
                if (empleadosString != null) {
                    empleadosArray = empleadosString.split(",");
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        return empleadosArray;
    }

    /**
     * Método para transformar el array de empleados en una matriz de objetos con los campos correspondientes.
     *
     * @param empleadosArray El array con la información de cada empleado.
     * @return Una matriz de objetos con los campos de inicial, sexo, edad y nivel.
     */
    public static Object[][] transformarEmpleadosAHojas(String[] empleadosArray) {
        Object[][] empleadosMatriz = new Object[empleadosArray.length][4];

        for (int i = 0; i < empleadosArray.length; i++) {
            String[] empleado = empleadosArray[i].split("_");
            empleadosMatriz[i][0] = empleado[0].substring(0, 3); // Iniciales
            empleadosMatriz[i][1] = empleado[1]; // Sexo
            empleadosMatriz[i][2] = Integer.parseInt(empleado[2]); // Edad
            empleadosMatriz[i][3] = Integer.parseInt(empleado[3]); // Nivel
        }

        return empleadosMatriz;
    }

    /**
     * Método para filtrar la matriz de empleados por un campo específico.
     *
     * @param empleadosMatriz La matriz con la información de los empleados.
     * @param campo           El índice del campo a filtrar (0 - Inicial, 1 - Sexo, 2 - Edad, 3 - Nivel).
     * @param valorCampo      El valor del campo por el cual filtrar.
     * @return Una matriz con los empleados filtrados.
     */
    public static Object[][] filtrarEmpleadosPorCampo(Object[][] empleadosMatriz, int campo, Object valorCampo) {
        Object[][] empleadosFiltrados = new Object[empleadosMatriz.length][4];
        int indiceFila = 0;

        for (int i = 0; i < empleadosMatriz.length; i++) {
            if (empleadosMatriz[i][campo].equals(valorCampo)) {
                for (int j = 0; j < 4; j++) {
                    empleadosFiltrados[indiceFila][j] = empleadosMatriz[i][j];
                }
                indiceFila++;
            }
        }

        return empleadosFiltrados;
    }

    /**
     * Método para calcular la edad media de un conjunto de empleados.
     *
     * @param empleadosMatriz La matriz con la información de los empleados.
     * @return La edad media de los empleados.
     */
    public static double calcularEdadMedia(Object[][] empleadosMatriz) {
        double sumaEdades = 0;
        for (int i = 0; i < empleadosMatriz.length; i++) {
            sumaEdades += (int) empleadosMatriz[i][2];
        }

        return sumaEdades / empleadosMatriz.length;
    }

    /**
     * Método para promocionar a todos los empleados de la matriz.
     * Si un empleado es promocionado, entonces su nivel aumenta en 1. Ojo! Si tiene el nivel máximo no puede promocionar más.
     *
     * @param empleadosMatriz La matriz con la información de los empleados.
     */
    public static void promocionarEmpleados(Object[][] empleadosMatriz) {
        for (int i = 0; i < empleadosMatriz.length; i++) {
            int nivelActual = (int) empleadosMatriz[i][3];
            if (nivelActual < 15) {
                empleadosMatriz[i][3] = nivelActual + 1;
            }
        }
    }

    /**
     * Método para imprimir la información de los empleados.
     *
     * @param empleadosMatriz La matriz con la información de los empleados.
     */
    public static void imprimirEmpleados(Object[][] empleadosMatriz) {
        for (int i = 0; i < empleadosMatriz.length; i++) {
            System.out.println(
                    "Iniciales: " + empleadosMatriz[i][0] +
                            ", Sexo: " + empleadosMatriz[i][1] +
                            ", Edad: " + empleadosMatriz[i][2] +
                            ", Nivel: " + empleadosMatriz[i][3]
            );
        }
    }
}
