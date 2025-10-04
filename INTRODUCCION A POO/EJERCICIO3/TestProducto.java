package EJERCICIO3;
public class TestProducto {
    public static void main(String[] args) {
        Producto prod = new Producto("galletas", 2, 40);
        System.out.println("El stock es: "+prod.stock);
        prod.vender(5);
        prod.reabastecer(8);
    }
}
