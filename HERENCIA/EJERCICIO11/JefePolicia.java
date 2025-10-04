package EJERCICIO11;
interface IPersona {
    String mostrar_datos_personales();
}

interface IEmpleado {
    int calcular_salario();
}

interface IPolicia {
    String mostrar_rango();
}

class Persona {
    protected String nombre;
    protected int edad;

    public Persona(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }
}

class Empleado {
    protected int sueldo;
    protected String codigo;

    public Empleado(int sueldo, String codigo) {
        this.sueldo = sueldo;
        this.codigo = codigo;
    }
}

class Policia {
    protected String grado;
    protected String unidad;

    public Policia(String grado, String unidad) {
        this.grado = grado;
        this.unidad = unidad;
    }
}

class JefePolicia extends Persona implements IPersona, IEmpleado, IPolicia {
    public int sueldo;
    public String codigo;
    public String grado;
    public String unidad;

    public JefePolicia(String nombre, int edad, int sueldo, String codigo, String grado, String unidad) {
        super(nombre, edad);
        this.sueldo = sueldo;
        this.codigo = codigo;
        this.grado = grado;
        this.unidad = unidad;
    }

    @Override
    public String mostrar_datos_personales() {
        return "Nombre: " + this.nombre + ", Edad: " + this.edad;
    }

    @Override
    public int calcular_salario() {
        return this.sueldo;
    }

    @Override
    public String mostrar_rango() {
        return "Grado: " + this.grado + ", Unidad: " + this.unidad;
    }

    public void mostrar_datos() {
        System.out.println("Jefe de Policía: " + this.nombre);
        System.out.println("Edad: " + this.edad);
        System.out.println("Código: " + this.codigo);
        System.out.println("Sueldo: " + this.sueldo);
        System.out.println("Grado: " + this.grado);
        System.out.println("Unidad: " + this.unidad);
    }
}

