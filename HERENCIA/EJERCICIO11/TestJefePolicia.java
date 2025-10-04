package EJERCICIO11;

public class TestJefePolicia {
    public static void main(String[] args) {
        JefePolicia jefe1 = new JefePolicia("Roberto Gómez", 45, 12000, "POL-001", "Coronel", "Unidad Táctica");
        JefePolicia jefe2 = new JefePolicia("Ana Martínez", 42, 15000, "POL-002", "Coronel", "Unidad de Investigación");

        System.out.println("JEFE 1:");
        jefe1.mostrar_datos();
        System.out.println("\nJEFE 2:");
        jefe2.mostrar_datos();

        if (jefe1.sueldo > jefe2.sueldo) {
            System.out.println("El jefe con mayor sueldo es: " + jefe1.nombre + " con un sueldo de " + jefe1.sueldo);
        } else if (jefe2.sueldo > jefe1.sueldo) {
            System.out.println("El jefe con mayor sueldo es: " + jefe2.nombre + " con un sueldo de " + jefe2.sueldo);
        } else {
            System.out.println("Ambos tienen el mismo sueldo: " + jefe1.sueldo);
        }

        if (jefe1.grado.equals(jefe2.grado)) {
            System.out.println("Ambos jefes tienen el mismo grado: " + jefe1.grado);
        } else {
            System.out.println("Los jefes tienen diferentes grados: " + jefe1.nombre + " es " + jefe1.grado + " y " + jefe2.nombre + " es " + jefe2.grado);
        }

        System.out.println("\nDatos personales de " + jefe1.nombre + ": " + jefe1.mostrar_datos_personales());
        System.out.println("Salario calculado: " + jefe1.calcular_salario());
        System.out.println("Rango: " + jefe1.mostrar_rango());
    }
}
