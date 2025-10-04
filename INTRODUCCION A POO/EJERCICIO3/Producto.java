package EJERCICIO3;

public class Producto {
    public String nombre;
    public double precio;
    public int stock;

    public Producto(String nombre, double precio, int stock){
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    public void vender(int cantidad){
        if (cantidad <= this.stock) {
            this.stock = this.stock - cantidad;
            System.out.println("se vendieron "+cantidad +" " +this.nombre+". Quedan: "+this.stock + " "+this.nombre);
            
        } else {
            System.out.println("No hay sufieciente producto");
        }
    }
    public void reabastecer(int cantidad){
        this.stock = this.stock + cantidad;
        System.out.println("se reabastecieron "+ cantidad +" "+ this.nombre +". Quedan: "+ this.stock + " "+this.nombre);
    }
}
