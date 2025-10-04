package EJERCICIO2;

class Videojuego {
    private String nombre;
    private String plataforma;
    private int cantidad;

    public Videojuego(String nombre, String plataforma, int cantidad) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidad = cantidad;
    }

    public Videojuego(String nombre, String plataforma) {
        this.nombre = nombre;
        this.plataforma = plataforma;
        this.cantidad = 0;
    }

    public int agregarJugadores() {
        this.cantidad += 1;
        return this.cantidad;
    }

    public int agregarJugadores(int cantidad) {
        this.cantidad += cantidad;
        return this.cantidad;
    }

    public void mostrar() {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Plataforma: " + this.plataforma);
        System.out.println("Cantidad: " + this.cantidad);
    }
}
