package EJERCICIO3;

public class TestMatriz {
    public static void main(String[] args) {
        Matriz m1 = new Matriz(null);

        double[][] cero = new double[10][10];
        Matriz m2 = new Matriz(cero);

        Matriz m3 = m1.sumar(m2);
        Matriz m4 = m1.restar(m2);

        System.out.println(m1.equals(m2));
        System.out.println(m1.equals(m3));
        System.out.println(m1.equals(m4));

        m1.mostrar();
    }
}
