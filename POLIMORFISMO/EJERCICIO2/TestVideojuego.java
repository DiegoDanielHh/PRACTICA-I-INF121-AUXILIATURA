package EJERCICIO2;

import java.util.Scanner;

public class TestVideojuego {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Videojuego v1 = new Videojuego("FIFA", "PlayStation", 2);
        Videojuego v2 = new Videojuego("Minecraft", "PC");

        System.out.println("Videojuego 1:");
        v1.mostrar();
        v1.agregarJugadores();
        System.out.println("\nDespués de agregar 1 jugador:");
        v1.mostrar();

        System.out.println("\nVideojuego 2:");
        v2.mostrar();
        System.out.print("\nIngrese la cantidad de jugadores a agregar: ");
        int num = sc.nextInt();
        v2.agregarJugadores(num);
        System.out.println("\nDespués de agregar jugadores:");
        v2.mostrar();

        sc.close();
    }
}
