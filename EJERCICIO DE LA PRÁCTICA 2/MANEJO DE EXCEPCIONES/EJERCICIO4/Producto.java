package EJERCICIO4;
import java.util.ArrayList;

class ProductoNoEncontradoException extends Exception {
    public ProductoNoEncontradoException(String mensaje) {
        super(mensaje);
    }
}

class StockInsuficienteException extends Exception {
    public StockInsuficienteException(String mensaje) {
        super(mensaje);
    }
}

class CodigoDuplicadoException extends Exception {
    public CodigoDuplicadoException(String mensaje) {
        super(mensaje);
    }
}

class ValorInvalidoException extends Exception {
    public ValorInvalidoException(String mensaje) {
        super(mensaje);
    }
}

class Producto {
    private String codigo;
    private String nombre;
    private double precio;
    private int stock;

    public Producto(String codigo, String nombre, double precio, int stock) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    public String getCodigo() { return codigo; }
    public String getNombre() { return nombre; }
    public double getPrecio() { return precio; }
    public int getStock() { return stock; }
    public void setStock(int stock) { this.stock = stock; }

    @Override
    public String toString() {
        return "Codigo:" + codigo +
               " Nombre:" + nombre +
               " Precio:" + precio + "Bs" +
               " Stock:" + stock;
    }
}

class Inventario {
    private ArrayList<Producto> productos;

    public Inventario() {
        productos = new ArrayList<>();
    }

    public void agregarProducto(String codigo, String nombre, double precio, int stock)
            throws CodigoDuplicadoException, ValorInvalidoException {

        for (Producto p : productos) {
            if (p.getCodigo().equals(codigo)) {
                throw new CodigoDuplicadoException("El código ya existe");
            }
        }

        if (precio < 0 || stock < 0) {
            throw new ValorInvalidoException("el precio y stock no pueden ser negativos");
        }

        Producto nuevo = new Producto(codigo, nombre, precio, stock);
        productos.add(nuevo);
    }

    public Producto buscarProducto(String codigo) throws ProductoNoEncontradoException {
        for (Producto p : productos) {
            if (p.getCodigo().equals(codigo)) {
                return p;
            }
        }
        throw new ProductoNoEncontradoException("Producto no encontrado");
    }

    public void venderProducto(String codigo, int cantidad)
            throws ProductoNoEncontradoException, StockInsuficienteException {

        Producto producto = buscarProducto(codigo);

        if (producto.getStock() >= cantidad) {
            producto.setStock(producto.getStock() - cantidad);
        } else {
            throw new StockInsuficienteException("No hay stock suficiente");
        }
    }

    public void mostrarInventario() {
        System.out.println("Inventario:");
        for (Producto p : productos) {
            System.out.println(p);
        }
    }
}
