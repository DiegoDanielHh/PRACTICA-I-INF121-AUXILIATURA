package EJERCICIO2;
public class TestBus1 {
    public static void main(String[] args) {
        Bus1 bus1 = new Bus1(25, 32);
        bus1.disponibles();
        bus1.subirPasajero(2);
        bus1.cobrar();
        bus1.disponibles();
    }
}