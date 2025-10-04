package EJERCICIO1;

public class TestPersona {
    public static void main(String[] args) {
        Persona pe = new Persona("juan", "perez", 1234566);
        System.out.println(pe);

        Cliente cl = new Cliente("pedro", "picapiedra", 12312312, 23, 191991);
        System.out.println(cl);

        Jefe je = new Jefe("pablo", "perez", 8776655, "Sucursal Centro", "galeria");
        System.out.println(je);
    }
}
