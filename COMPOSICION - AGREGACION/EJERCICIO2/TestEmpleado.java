package EJERCICIO2;
import java.util.ArrayList;


public class TestEmpleado {
    public static void main(String[] args) {
        Departamento dep1 = new Departamento("Recursos humanos", "Administracion");
        Departamento dep2 = new Departamento("Investigación", "Desarrollo");

        Empleado e1 = new Empleado("Ana", "Analista", 3000);
        Empleado e2 = new Empleado("Luis", "Asistente", 2500);
        Empleado e3 = new Empleado("Marta", "Jefa", 5000);
        Empleado e4 = new Empleado("Pablo", "Reclutador", 2800);
        Empleado e5 = new Empleado("Sonia", "Psicóloga", 3200);

        ArrayList<Empleado> vectorEmpleadosd1 = new ArrayList<>();
        vectorEmpleadosd1.add(e1);
        vectorEmpleadosd1.add(e2);
        vectorEmpleadosd1.add(e3);
        vectorEmpleadosd1.add(e4);
        vectorEmpleadosd1.add(e5);

        dep1.setEmpleados(vectorEmpleadosd1);

        dep1.mostrarEmpleados();
        dep2.mostrarEmpleados();

        System.out.println("Aplicando el cambio de salario");
        dep1.cambioSalario(4000);
        dep1.mostrarEmpleados();

        System.out.println("VERIFICACION DE EMPLEADOS: ");
        int cont = 0;
        for (Empleado e : dep1.getEmpleados()) {
            if (dep2.getEmpleados().contains(e)) {
                cont++;
            }
        }

        if (cont > 0) {
            System.out.println("Existe un empleado de dep1 en dep2");
        } else {
            System.out.println("No existe un empleado de dep1 en dep2");
        }

        System.out.println("MOVIENDO EMPLEADOS");
        for (Empleado e : dep1.getEmpleados()) {
            dep2.getEmpleados().add(e);
        }

        dep1.setEmpleados(new ArrayList<>());

        dep1.mostrarEmpleados();
        dep2.mostrarEmpleados();
    }
}

