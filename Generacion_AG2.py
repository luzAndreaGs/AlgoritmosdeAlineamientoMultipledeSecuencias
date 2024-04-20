import random
from Individuo import Individuo

class Generacion:
    def __init__(self, secuencias):
        self.num_individuos = 4
        self.poblacion = [Individuo(secuencias) for _ in range(self.num_individuos)]
        self.num_secuencias = len(self.poblacion[0].secuencias)
        self.secuencias_originales = secuencias

    def ordenar(self):
        self.poblacion.sort(key=lambda x: x.calificar(), reverse=True)

    def alinear_secuencias(self):
        max_len_secuencia = max(len(individuo.secuencias[0]) for individuo in self.poblacion)
        for individuo in self.poblacion:
            for i in range(self.num_secuencias):
                secuencia = individuo.secuencias[i]
                secuencia += ['-'] * (max_len_secuencia - len(secuencia))

    def seleccion_torneo(self, n):
        participantes = random.sample(self.poblacion, n)
        return participantes

    def reproducir(self):
        hijos = []
        # Seleccionar una pareja de padres
        padres = self.seleccion_torneo(4)
        indice_padre1 = self.poblacion.index(max(padres, key=lambda x: x.calificar()))
        padres.remove(padres[indice_padre1])
        indice_padre2 = self.poblacion.index(max(padres, key=lambda x: x.calificar()))
        
        # Generar cuatro hijos a partir de la pareja de padres
        for _ in range(2):
            hijo1 = self.hijo(indice_padre1, indice_padre2)
            hijo2 = self.hijo(indice_padre2, indice_padre1)
            hijos.extend([hijo1, hijo2])

        self.poblacion = hijos


    def hijo(self, padre1, padre2):
        sec_hijo = []

        for i in range(self.num_secuencias):
            secuencia_padre1 = self.poblacion[padre1].secuencias[i]
            secuencia_padre2 = self.poblacion[padre2].secuencias[i]

            # Alinear las secuencias con caracteres '-' si es necesario
            len_padre1 = len(secuencia_padre1)
            len_padre2 = len(secuencia_padre2)
            max_len_secuencia = max(len_padre1, len_padre2)
            secuencia_padre1 += '-' * (max_len_secuencia - len_padre1)
            secuencia_padre2 += '-' * (max_len_secuencia - len_padre2)

            # Crear la secuencia del hijo
            secuencia_hijo_i = ''
            for j in range(max_len_secuencia):
                if secuencia_padre1[j] == secuencia_padre2[j] or [secuencia_padre2[j] == '-' and secuencia_padre1[j] != '-']:
                    secuencia_hijo_i += secuencia_padre1[j]  
                # Si ambos padres tienen el mismo carácter o también, si el carácter del padre2 es un gap y en la
                # misma posicion el caracter del padre1 es alfabético, el hijo hereda el carácter del padre1
                else:
                    secuencia_hijo_i += secuencia_padre2[j]  # En otro caso, el hijo hereda el carácter del padre2

            sec_hijo.append(secuencia_hijo_i)

        return Individuo(sec_hijo)
    
    def validar_secuencias(self, secuencias_hijo, secuencias_originales):
        for secuencia_hijo, secuencia_original in zip(secuencias_hijo, secuencias_originales):
            secuencia_hijo_sin_gaps = ''.join([c for c in secuencia_hijo if c.isalpha()])
            if secuencia_hijo_sin_gaps != secuencia_original:
                return False
        return True