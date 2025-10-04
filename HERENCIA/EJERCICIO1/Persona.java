package EJERCICIO1;
public class Persona {
    protected String nombre;
    protected String apellido;
    protected int ci;

    public Persona(String nombre, String apellido, int ci) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.ci = ci;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Apellido: " + apellido + ", ci: " + ci;
    }
}

class Cliente extends Persona {
    private int nroCompra;
    private int idCliente;

    public Cliente(String nombre, String apellido, int ci, int nroCompra, int idCliente) {
        super(nombre, apellido, ci);
        this.nroCompra = nroCompra;
        this.idCliente = idCliente;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Apellido: " + apellido + ", ci: " + ci +
               ", NroCompra: " + nroCompra + ", ID: " + idCliente;
    }
}

class Jefe extends Persona {
    private String sucursal;
    private String tipo;

    public Jefe(String nombre, String apellido, int ci, String sucursal, String tipo) {
        super(nombre, apellido, ci);
        this.sucursal = sucursal;
        this.tipo = tipo;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Apellido: " + apellido + ", ci: " + ci +
               ", sucursal: " + sucursal + ", tipo: " + tipo;
    }
}

