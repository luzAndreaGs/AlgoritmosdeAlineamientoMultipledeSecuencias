import random

class Individuo:
    def __init__(self, entrada):
        self.secuencias = [list(i) for i in entrada]
        self.maxAgregar = 3  # Número máximo de GAPS que se pueden agregar en la mutación
        self.mutar()

    def calificar(self):
        cal = 0
        for i in range(len(self.secuencias[0])):
            letras = set()
            for j in range(len(self.secuencias)):
                if self.secuencias[j][i] == '-':
                    cal -= 1  # Si se encuentra un GAP, se restan puntos
                elif self.secuencias[j][i] in letras:
                    cal += 5  # Si encuentra una letra repetida en la columna, se suman 5 puntos
                else:
                    letras.add(self.secuencias[j][i])
                    cal += 1  # Se agregan letras y se suma un punto
        return cal

    def mutar(self):
        for i in range(len(self.secuencias)):
            gaps = [j for j, val in enumerate(self.secuencias[i]) if val == '-']

            # Posiciones que se van a eliminar
            eliminar = random.sample(gaps, min(self.maxAgregar, len(gaps)))

            # Posiciones que se van a agregar
            agregar = random.sample(range(len(self.secuencias[i])), self.maxAgregar)

            self.modificar_gaps(i, eliminar, agregar)

        self.alinear()
        self.eliminar()

    def modificar_gaps(self, i, eliminar, agregar):
        secuencia = self.secuencias[i]
        nuevo = []

        for j in range(len(secuencia)):
            if j in eliminar:
                continue
            nuevo.append(secuencia[j])
            if j in agregar:
                nuevo.append('-')

        self.secuencias[i] = nuevo

    def alinear(self):
        max_len = max(len(seq) for seq in self.secuencias)
        for i in range(len(self.secuencias)):
            self.secuencias[i] += ['-'] * (max_len - len(self.secuencias[i]))

    def eliminar(self):
        cols_a_eliminar = set()
        for i in range(len(self.secuencias[0])):
            if all(seq[i] == '-' for seq in self.secuencias):
                cols_a_eliminar.add(i)

        for col in sorted(cols_a_eliminar, reverse=True):
            for i in range(len(self.secuencias)):
                del self.secuencias[i][col]