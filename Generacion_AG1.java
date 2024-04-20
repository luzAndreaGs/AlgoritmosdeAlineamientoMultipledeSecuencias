package optimización;
import java.util.*;

public class Generacion_AG1 {
    int num = 200; // Usamos un número múltiplo de 4 para la reproducción, cada pareja tiene 4 hijos
    Individuo_AG1[] poblacion = new Individuo_AG1[num];
    
    public Generacion_AG1(String[] entrada) {
        char[][] x = new char[entrada.length][];
        for (int j = 0; j < entrada.length; j++) {
            x[j]=entrada[j].toCharArray();
        }
        
        for (int i = 0; i < num; i++) {
            poblacion[i] = new Individuo_AG1(x);
        }
    }

    public void Ordenar() {// ordena la poblacion dependiendo su calificacion
        for (int i = 0; i < num; i++) {
            int x = i;
            for (int j = i - 1; j >= 0; j--) {
                if (poblacion[x].Calificar() > poblacion[j].Calificar()) {
                    Individuo_AG1 temp = poblacion[x];
                    poblacion[x] = poblacion[j];
                    poblacion[j] = temp;
                    x = j;
                }
            }
        }
    }
    
    public int Letras(int i){//cuenta las letras, se dividen las secuencias de los individuos en la misma letra, ignorar gaps
        int cont = 0;
        for (char j : poblacion[0].secuencias[i]) {
            if(Character.isLetter(j))
                cont++;
        }
        return cont;
    }

    private Individuo_AG1 seleccionPorRuleta() {
        double[] probabilidades = new double[poblacion.length];
        double sumaTotal = 0;
        // Calcular la suma total de las calificaciones y asignar probabilidades proporcionales
        for (int i = 0; i < poblacion.length; i++) {
            sumaTotal += poblacion[i].Calificar();
        }
        // Calcular la probabilidad de selección para cada individuo
        for (int i = 0; i < poblacion.length; i++) {
            probabilidades[i] = poblacion[i].Calificar() / sumaTotal;
        }
        // Generar un número aleatorio para la selección en el rango (0,1]
        Random random = new Random();
        double valorSeleccionado = random.nextDouble();
        double sumaProbabilidades = 0;
        // Iterar sobre las probabilidades acumuladas y seleccionar el individuo correspondiente
        for (int i = 0; i < poblacion.length; i++) {
            sumaProbabilidades += probabilidades[i];
            if (valorSeleccionado <= sumaProbabilidades) {
                return poblacion[i];
            }
        }
        // En caso de que no se haya seleccionado ningún individuo, se devuelve uno aleatorio
        return poblacion[new Random().nextInt(poblacion.length)];
    }
 
        private Individuo_AG1 Hijo(Individuo_AG1 padre1, Individuo_AG1 padre2) Individuo_AG1

    public void Reproducir() {
        Individuo[] hijos = new Individuo[num];
        for (int i = 0; i < num; i++) {
            Individuo padre1 = seleccionPorRuleta();
            Individuo padre2 = seleccionPorRuleta();
            hijos[i] = Hijo(padre1, padre2);
        }
        poblacion = hijos;
    }
    
    public String verificarSecuencia(Individuo hijo) {
        StringBuilder sb = new StringBuilder();
        for (char[] secuencia : hijo.secuencias) {
            for (char c : secuencia) {
                if (c != '-') {
                    sb.append(c);
                }
            }
        }
        String secuenciaHijo = sb.toString();

        boolean integridad = true;
        for (Individuo individuo : poblacion) {
            StringBuilder sbOriginal = new StringBuilder();
            for (char[] secuencia : individuo.secuencias) {
                for (char c : secuencia) {
                    if (c != '-') {
                        sbOriginal.append(c);
                    }
                }
            }
            String secuenciaOriginal = sbOriginal.toString();
            if (!secuenciaHijo.equals(secuenciaOriginal)) {
                integridad = false;
                break;
            }
        }

        if (integridad) {
            return "Individuo verificado correctamente";
        } else {
            return "Error en la secuencia";
        }
    }
}