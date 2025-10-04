package EJERCICIO2;
public class Bus1 {
    private int cantPasajeros;
    private int asientos;

    public Bus1(int cantPasajeros, int asientos) {
        this.cantPasajeros = cantPasajeros;
        this.asientos = asientos;
    }

    public void disponibles() {
        int dis = asientos - cantPasajeros;
        System.out.println("Asientos disponibles: " + dis + " asientos");
    }

    public void subirPasajero(int nuevos) {
        if (cantPasajeros + nuevos <= asientos) {
            cantPasajeros += nuevos;
            System.out.println(nuevos + " pasajeros subieron, el total es " + cantPasajeros);
        } else {
            System.out.println("No hay más asientos para los " + nuevos + " pasajeros");
        }
    }

    public void cobrar() {
        double total = 1.50 * cantPasajeros;
        System.out.println("Se cobró a 1,50 y el total es " + total + " Bs");
    }
}
