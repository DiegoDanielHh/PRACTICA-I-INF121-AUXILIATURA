package EJERCICIO2;

import java.util.ArrayList;

class Empleado {
    private String nombre;
    private String cargo;
    private double sueldo;

    public Empleado(String nombre, String cargo, double sueldo) {
        this.nombre = nombre;
        this.cargo = cargo;
        this.sueldo = sueldo;
    }

    public String getNombre() {
        return nombre;
    }

    public String getCargo() {
        return cargo;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double nuevosueldo) {
        this.sueldo = nuevosueldo;
    }
}

class Departamento {
    private String nombre;
    private String area;
    private ArrayList<Empleado> empleados;

    public Departamento(String nombre, String area) {
        this.nombre = nombre;
        this.area = area;
        this.empleados = new ArrayList<>();
    }

    public void mostrarEmpleados() {
        System.out.println("Departamento: " + nombre + " Area: " + area);
        if (empleados.isEmpty()) {
            System.out.println("No existen empleados");
        } else {
            for (Empleado e : empleados) {
                System.out.println("nombre: " + e.getNombre() + ", cargo: " + e.getCargo() +
                                   " y sueldo: " + e.getSueldo());
            }
        }
    }

    public void cambioSalario(double nuevosalario) {
        for (Empleado e : empleados) {
            e.setSueldo(nuevosalario);
        }
    }

    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(ArrayList<Empleado> vectorEmpleados) {
        this.empleados = vectorEmpleados;
    }
}

