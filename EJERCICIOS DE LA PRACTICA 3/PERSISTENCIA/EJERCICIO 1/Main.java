import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

class Charango {
    public String material;
    public int nroCuerdas;
    public List<Boolean> cuerdas;

    public Charango() {
        this.material = "";
        this.nroCuerdas = 0;
        this.cuerdas = new ArrayList<>();
    }

    public Charango(String material, int nroCuerdas, List<Boolean> cuerdas) {
        this.material = material;
        this.nroCuerdas = nroCuerdas;
        this.cuerdas = cuerdas;
    }

    public static void guardarCharangos(List<Charango> lista, String archivo) {
        try {
            Gson gson = new Gson();
            String json = gson.toJson(lista);
            FileWriter writer = new FileWriter(archivo);
            writer.write(json);
            writer.close();
            System.out.println("Archivo guardado correctamente.");
        } catch (Exception e) {
            System.out.println("Error al guardar: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static List<Charango> cargarCharangos(String archivo) {
        try {
            Gson gson = new Gson();
            FileReader reader = new FileReader(archivo);
            Type listType = new TypeToken<List<Charango>>(){}.getType();
            List<Charango> lista = gson.fromJson(reader, listType);
            reader.close();
            System.out.println("Archivo cargado correctamente.");
            return lista != null ? lista : new ArrayList<>();
        } catch (FileNotFoundException e) {
            System.out.println("El archivo no existe.");
            return new ArrayList<>();
        } catch (Exception e) {
            System.out.println("Error al cargar: " + e.getMessage());
            e.printStackTrace();
            return new ArrayList<>();
        }
    }

    public static List<Charango> eliminarCharangosDefectuosos(List<Charango> lista) {
        List<Charango> nuevaLista = new ArrayList<>();
        for (Charango c : lista) {
            int count = 0;
            for (Boolean cuerda : c.cuerdas) {
                if (!cuerda) count++;
            }
            if (count <= 6) {
                nuevaLista.add(c);
            }
        }
        return nuevaLista;
    }

    public static List<Charango> listarPorMaterial(List<Charango> lista, String material) {
        List<Charango> resultado = new ArrayList<>();
        for (Charango c : lista) {
            if (c.material.equals(material)) {
                resultado.add(c);
            }
        }
        return resultado;
    }

    public static List<Charango> buscarCon10Cuerdas(List<Charango> lista) {
        List<Charango> resultado = new ArrayList<>();
        for (Charango c : lista) {
            if (c.nroCuerdas == 10) {
                resultado.add(c);
            }
        }
        return resultado;
    }

    public static List<Charango> ordenarPorMaterial(List<Charango> lista) {
        int n = lista.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (lista.get(j).material.compareTo(lista.get(j + 1).material) > 0) {
                    Charango temp = lista.get(j);
                    lista.set(j, lista.get(j + 1));
                    lista.set(j + 1, temp);
                }
            }
        }
        return lista;
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println("Iniciando programa...");
        
        List<Charango> charangos = new ArrayList<>();
        
        List<Boolean> cuerdas1 = new ArrayList<>();
        for (int i = 0; i < 10; i++) cuerdas1.add(true);
        charangos.add(new Charango("madera", 10, cuerdas1));
        
        List<Boolean> cuerdas2 = new ArrayList<>();
        for (int i = 0; i < 7; i++) cuerdas2.add(false);
        cuerdas2.add(true);
        charangos.add(new Charango("plastico", 8, cuerdas2));
        
        List<Boolean> cuerdas3 = new ArrayList<>();
        for (int i = 0; i < 9; i++) cuerdas3.add(true);
        cuerdas3.add(false);
        charangos.add(new Charango("madera", 10, cuerdas3));
        
        List<Boolean> cuerdas4 = new ArrayList<>();
        for (int i = 0; i < 10; i++) cuerdas4.add(true);
        charangos.add(new Charango("metal", 10, cuerdas4));
        
        System.out.println("Charangos creados: " + charangos.size());
        
        Charango.guardarCharangos(charangos, "charangos.json");
        List<Charango> cargados = Charango.cargarCharangos("charangos.json");
        
        System.out.println("Charangos cargados: " + cargados.size());
        
        List<Charango> filtrados = Charango.eliminarCharangosDefectuosos(cargados);
        List<Charango> madera = Charango.listarPorMaterial(filtrados, "madera");
        List<Charango> diezCuerdas = Charango.buscarCon10Cuerdas(filtrados);
        List<Charango> ordenados = Charango.ordenarPorMaterial(filtrados);
        
        System.out.println("\nResultados:");
        System.out.println("Charangos válidos: " + filtrados.size());
        System.out.println("Hechos de madera: " + madera.size());
        System.out.println("Con 10 cuerdas: " + diezCuerdas.size());
        
        System.out.println("\nMateriales ordenados:");
        for (Charango c : ordenados) {
            System.out.println(c.material);
        }
        
        System.out.println("\nPrograma finalizado.");
    }
}