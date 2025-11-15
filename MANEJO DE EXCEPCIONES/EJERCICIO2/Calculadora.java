package EJERCICIO2;
public class Calculadora {

    public double sumar(double a, double b) {
        return a + b;
    }

    public double restar(double a, double b) {
        return a - b;
    }

    public double multiplicar(double a, double b) {
        return a * b;
    }

    public double dividir(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("No se puede dividir entre cero");
        }
        return a / b;
    }

    public int convertirAEntero(String cadena) {
        return Integer.parseInt(cadena);
    }

    public static void main(String[] args) {
        Calculadora calc = new Calculadora();

        System.out.println("Suma: " + calc.sumar(5, 3));
        System.out.println("Resta: " + calc.restar(10, 4));
        System.out.println("Multiplicación: " + calc.multiplicar(6, 7));

        try {
            System.out.println("División: " + calc.dividir(10, 0));
        } catch (ArithmeticException e) {
            System.out.println("Error!!!!!!!!!!: " + e.getMessage());
        }

        try {
            int numero = calc.convertirAEntero("123456");
            System.out.println("Número convertido: " + numero);

            numero = calc.convertirAEntero("abcsdfs");
            System.out.println("Número convertido: " + numero);
        } catch (NumberFormatException e) {
            System.out.println("Error!!!!!!!!!!!: " + e.getMessage());
        }
    }
}

