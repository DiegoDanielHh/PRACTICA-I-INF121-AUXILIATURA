package EJERCICIO3;
public class Matriz {
    double[][] matriz;

    public Matriz(double[][] valores) {
        matriz = new double[10][10];
        if (valores == null) {
            for (int i = 0; i < 10; i++) {
                matriz[i][i] = 1.0;
            }
        } else {
            for (int i = 0; i < 10; i++) {
                for (int j = 0; j < 10; j++) {
                    matriz[i][j] = valores[i][j];
                }
            }
        }
    }

    public Matriz sumar(Matriz otra) {
        double[][] resultado = new double[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado[i][j] = this.matriz[i][j] + otra.matriz[i][j];
            }
        }
        return new Matriz(resultado);
    }

    public Matriz restar(Matriz otra) {
        double[][] resultado = new double[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                resultado[i][j] = this.matriz[i][j] - otra.matriz[i][j];
            }
        }
        return new Matriz(resultado);
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Matriz)) {
            return false;
        }
        Matriz otra = (Matriz) obj;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (this.matriz[i][j] != otra.matriz[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public void mostrar() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.printf("%.1f ", matriz[i][j]);
            }
            System.out.println();
        }
    }
}

