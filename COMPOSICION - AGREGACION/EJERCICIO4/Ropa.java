package EJERCICIO4;

import java.util.ArrayList;

class Ropa {
    private String tipo;
    private String material;

    public Ropa(String tipo, String material) {
        this.tipo = tipo;
        this.material = material;
    }

    public String getTipo() {
        return tipo;
    }

    public String getMaterial() {
        return material;
    }
}

class Ropero {
    private String material;
    private ArrayList<Ropa> ropa;
    private int nroRopas;

    public Ropero(String material) {
        this.material = material;
        this.ropa = new ArrayList<>();
        this.nroRopas = 0;
    }

    public void adicionarPrendas(int N, ArrayList<Ropa> prendas) {
        int contador = 0;
        for (Ropa prenda : prendas) {
            if (contador < N && ropa.size() < 20) {
                ropa.add(prenda);
                nroRopas++;
                contador++;
            } else {
                break;
            }
        }
    }

    public void eliminarPrendas(String x, String y) {
        int i = 0;
        while (i < ropa.size()) {
            Ropa prenda = ropa.get(i);
            if (prenda.getMaterial().equals(x) || prenda.getTipo().equals(y)) {
                ropa.remove(i);
                nroRopas--;
            } else {
                i++;
            }
        }
    }

    public void mostrar(String x, String y) {
        System.out.println("Las prendas son:");
        for (Ropa prenda : ropa) {
            if (prenda.getMaterial().equals(x) && prenda.getTipo().equals(y)) {
                System.out.println("Tipo: " + prenda.getTipo() + ", Material: " + prenda.getMaterial());
            }
        }
    }

    public int getNroRopas() {
        return nroRopas;
    }
}


