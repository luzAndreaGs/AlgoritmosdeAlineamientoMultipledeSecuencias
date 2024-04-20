class Archivos:
    def leertxt(self, direccion):
        txt = ""
        try:
            with open(direccion, 'r') as file:
                next(file)  # Saltar la primera línea
                for line in file:
                    txt += line.strip()
        except FileNotFoundError as ex:
            print("Error al abrir el archivo:", ex)
        return txt