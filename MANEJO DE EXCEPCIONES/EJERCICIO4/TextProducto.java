package EJERCICIO4;


public class TextProducto {
    public static void main(String[] args) {
        Inventario inv = new Inventario();

        try {
            inv.agregarProducto("P001", "Laptop", 1500, 10);
            inv.agregarProducto("P002", "Mouse", 20, 50);
            inv.agregarProducto("P003", "Teclado", 30, 30);
        } catch (CodigoDuplicadoException | ValorInvalidoException e) {
            System.out.println("Error al agregar producto: " + e.getMessage());
        }

        inv.mostrarInventario();

        try {
            System.out.println("\nBuscando producto P002:");
            System.out.println(inv.buscarProducto("P002"));
        } catch (ProductoNoEncontradoException e) {
            System.out.println("Error: " + e.getMessage());
        }

        try {
            System.out.println("\nVendiendo 5 laptops");
            inv.venderProducto("P001", 5);
            System.out.println(inv.buscarProducto("P001"));
        } catch (ProductoNoEncontradoException | StockInsuficienteException e) {
            System.out.println("Error en venta: " + e.getMessage());
        }

        try {
            System.out.println("\nVendiendo 50 teclados");
            inv.venderProducto("P003", 50);
        } catch (StockInsuficienteException | ProductoNoEncontradoException e) {
            System.out.println("Error en venta: " + e.getMessage());
        }

        try {
            System.out.println("\nBuscando producto P999:");
            System.out.println(inv.buscarProducto("P999"));
        } catch (ProductoNoEncontradoException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
