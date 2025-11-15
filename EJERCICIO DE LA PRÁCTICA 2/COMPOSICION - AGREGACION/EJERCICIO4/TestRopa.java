package EJERCICIO4;

import java.util.ArrayList;

public class TestRopa {
    public static void main(String[] args) {
        Ropa r1 = new Ropa("abrigo", "pelo de oso");
        Ropa r2 = new Ropa("deportivo", "hilo sintetico");
        Ropa r3 = new Ropa("camisa", "algodon");

        Ropero ropero1 = new Ropero("madera");

        ArrayList<Ropa> prendas = new ArrayList<>();
        prendas.add(r1);
        prendas.add(r2);
        prendas.add(r3);

        ropero1.adicionarPrendas(4, prendas);

        System.out.println("Total de prendas: " + ropero1.getNroRopas());
        ropero1.mostrar("algodon", "camisa");

        // Opcional: ejemplo de eliminar
        ropero1.eliminarPrendas("pelo de oso", "deportivo");
        System.out.println("\nDespués de eliminar algunas prendas:");
        System.out.println("Total de prendas: " + ropero1.getNroRopas());
        ropero1.mostrar("algodon", "camisa");
    }
}
