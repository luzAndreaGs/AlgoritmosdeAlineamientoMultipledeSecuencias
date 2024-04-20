from Archivos import Archivos
from Generacion import Generacion
import time

class Algoritmo:
    def main(self):
        ruta_archivo_1 = "C:\\Users\\Luz Andrea\\Documentos escuela\\Analisis y Modelacion\\Escherichia coli strain.txt"
        ruta_archivo_2 = "C:\\Users\\Luz Andrea\\Documentos escuela\\Analisis y Modelacion\\Enterococcus faecalis strain.txt"
        ruta_archivo_3 = "C:\\Users\\Luz Andrea\\Documentos escuela\\Analisis y Modelacion\\Porphyromonas gingivalis strain.txt"
        ruta_archivo_4 = "C:\\Users\\Luz Andrea\\Documentos escuela\\Analisis y Modelacion\\Helicobacter pylori isolate.txt"
        ruta_archivo_5 = "C:\\Users\\Luz Andrea\\Documentos escuela\\Analisis y Modelacion\\Staphylococcus aureus strain.txt"
        ruta_archivo_6 = "C:\\Users\\Luz Andrea\\Documentos escuela\\Analisis y Modelacion\\Bacteroides fragilis strain.txt"
        
        # Instancia de la clase Archivos para leer el contenido de los archivos
        archivos = Archivos()

        secuencia_1 = archivos.leertxt(ruta_archivo_1)
        secuencia_2 = archivos.leertxt(ruta_archivo_2)
        secuencia_3 = archivos.leertxt(ruta_archivo_3)
        secuencia_4 = archivos.leertxt(ruta_archivo_4)
        secuencia_5 = archivos.leertxt(ruta_archivo_5)
        secuencia_6 = archivos.leertxt(ruta_archivo_6)

        #secuencias_originales = [secuencia_1, secuencia_2, secuencia_3]
        secuencias_originales = ["anticonstitucional","paleontologia","desproporcionalidad","interdisciplinario"]

        obj = Generacion(secuencias_originales)
        obj.ordenar()
        for x in obj.poblacion:
            for y in x.secuencias:
                print(" ".join(y))
            print(x.calificar(),"\n")
        print("\nHijos")
        for _ in range(10):
            print("╔══════════════════╗")
            print("    REPRODUCCION")
            print("╚══════════════════╝")
            obj.reproducir()
            obj.ordenar()
            for x in obj.poblacion:
                for y in x.secuencias:
                    print(" ".join(y))
                print(x.calificar())
                resultado = "Individuo verificado correctamente\n" if obj.validar_secuencias(x.secuencias, secuencias_originales) else "Individuo no valido\n"
                print(resultado)

#Se ejecuta el temporizador
start_time=time.time()

# Instanciar y ejecutar el método main
Algoritmo().main()

#Finaliza e imprime el tiempo de ejecucion
end_time = time.time()  # Tiempo final
execution_time = end_time - start_time  # Tiempo total de ejecución
print("\nTiempo de ejecución:", execution_time, "segundos")