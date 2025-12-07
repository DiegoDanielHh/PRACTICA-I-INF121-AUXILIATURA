import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

class Trabajador {
    private String nombre;
    private int carnet;
    private double salario;

    public Trabajador() {
        this.nombre = "";
        this.carnet = 0;
        this.salario = 0.0;
    }

    public Trabajador(String nombre, int carnet, double salario) {
        this.nombre = nombre;
        this.carnet = carnet;
        this.salario = salario;
    }

    public Map<String, Object> convertirADiccionario() {
        Map<String, Object> datos = new HashMap<>();
        datos.put("nombre", this.nombre);
        datos.put("carnet", this.carnet);
        datos.put("salario", this.salario);
        return datos;
    }

    public void convertirANormal(Map<String, Object> datos) {
        this.nombre = (String) datos.get("nombre");
        this.carnet = ((Number) datos.get("carnet")).intValue();
        this.salario = ((Number) datos.get("salario")).doubleValue();
    }

    public void aumentarSalario(double aumento) {
        this.salario += aumento;
    }

    public double obtenerSalario() {
        return this.salario;
    }

    public void mostrar() {
        System.out.println(this.nombre + " " + this.carnet + " " + this.salario);
    }

    public String getNombre() {
        return nombre;
    }

    public int getCarnet() {
        return carnet;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}

class ArchivoTrabajador {
    private String nombreArch;

    public ArchivoTrabajador() {
        this.nombreArch = "trabajadores.json";
    }

    public void crearArchivo() {
        try {
            Gson gson = new Gson();
            FileWriter writer = new FileWriter(nombreArch);
            writer.write("[]");
            writer.close();
            System.out.println("Archivo creado");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void guardarTrabajador(Trabajador t) {
        List<Map<String, Object>> datos;
        try {
            Gson gson = new Gson();
            FileReader reader = new FileReader(nombreArch);
            Type listType = new TypeToken<List<Map<String, Object>>>(){}.getType();
            datos = gson.fromJson(reader, listType);
            reader.close();
            if (datos == null) {
                datos = new ArrayList<>();
            }
        } catch (FileNotFoundException e) {
            datos = new ArrayList<>();
        } catch (Exception e) {
            datos = new ArrayList<>();
        }

        datos.add(t.convertirADiccionario());

        try {
            Gson gson = new Gson();
            FileWriter writer = new FileWriter(nombreArch);
            writer.write(gson.toJson(datos));
            writer.close();
            System.out.println("Guardado");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void aumentaSalario(double a, Trabajador t) {
        t.aumentarSalario(a);
        System.out.println("Salario aumentado");
    }

    public void buscarMayorSalario() {
        try {
            Gson gson = new Gson();
            FileReader reader = new FileReader(nombreArch);
            Type listType = new TypeToken<List<Map<String, Object>>>(){}.getType();
            List<Map<String, Object>> datos = gson.fromJson(reader, listType);
            reader.close();

            Map<String, Object> mayor = null;
            for (Map<String, Object> d : datos) {
                if (mayor == null || ((Number) d.get("salario")).doubleValue() > ((Number) mayor.get("salario")).doubleValue()) {
                    mayor = d;
                }
            }
            if (mayor != null) {
                System.out.println(mayor.get("nombre") + " " + mayor.get("carnet") + " " + mayor.get("salario"));
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void ordenarPorSalario() {
        try {
            Gson gson = new Gson();
            FileReader reader = new FileReader(nombreArch);
            Type listType = new TypeToken<List<Map<String, Object>>>(){}.getType();
            List<Map<String, Object>> datos = gson.fromJson(reader, listType);
            reader.close();

            int n = datos.size();
            for (int i = 0; i < n - 1; i++) {
                for (int j = 0; j < n - i - 1; j++) {
                    double salarioJ = ((Number) datos.get(j).get("salario")).doubleValue();
                    double salarioJ1 = ((Number) datos.get(j + 1).get("salario")).doubleValue();
                    if (salarioJ > salarioJ1) {
                        Map<String, Object> temp = datos.get(j);
                        datos.set(j, datos.get(j + 1));
                        datos.set(j + 1, temp);
                    }
                }
            }

            for (Map<String, Object> d : datos) {
                System.out.println(d.get("nombre") + " " + d.get("carnet") + " " + d.get("salario"));
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Trabajador t1 = new Trabajador("Ana", 123, 2500.0);
        Trabajador t2 = new Trabajador("Luis", 456, 3200.0);
        Trabajador t3 = new Trabajador("Sofia", 789, 2800.0);

        ArchivoTrabajador archivo = new ArchivoTrabajador();
        archivo.crearArchivo();

        archivo.guardarTrabajador(t1);
        archivo.guardarTrabajador(t2);
        archivo.guardarTrabajador(t3);

        archivo.aumentaSalario(500, t1);
        archivo.guardarTrabajador(t1);

        archivo.buscarMayorSalario();
        archivo.ordenarPorSalario();
    }
}