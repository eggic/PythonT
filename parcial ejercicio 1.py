class Biblioteca:
    def __init__(self):
        self.alumno = ""
        self.codigo = 0
        self.libro = ""
        self.fecha = ""
        self.carrera = ""
        self.fechaentrega = ""
        self.sancion = 10  # Sanción base por mes
        self.meses_retraso = 0

    def retrasos(self):
        if self.meses_retraso == 1:
            total_sancion = self.meses_retraso * self.sancion
            print(f"El libro lleva {self.meses_retraso} mes sin ser devuelto, debe pagar ${total_sancion}")
        elif self.meses_retraso == 2:
            total_sancion = self.meses_retraso * self.sancion
            print(f"El libro lleva {self.meses_retraso} meses sin ser devuelto, debe pagar ${total_sancion}")
        elif self.meses_retraso >= 3:
            print("Te has excedido en los meses de retraso, por lo tanto ya no podrás solicitar libros")
        else:
            print("El libro ha sido devuelto a tiempo. No hay sanción.")

    def registro(self):
        self.alumno = input("Ingrese el nombre del alumno: ")
        self.codigo = input("Ingrese el código del estudiante: ")
        self.libro = input("Libro que se prestará: ")
        self.fecha = input("Ingrese la fecha en que se prestó el libro: ")
        self.carrera = input("Ingrese la carrera del alumno: ")
        self.fechaentrega = input("Ingrese la fecha de entrega: ")
        
        # Simular cálculo de meses de retraso (esto debería ser calculado según la fecha actual y fecha de entrega)
        # Aquí se puede reemplazar con una lógica real basada en fechas
        self.meses_retraso = int(input("Ingrese el número de meses de retraso: "))

    def mostrardato(self):
        print("--------------------------------------------")
        print("La lectura es importante")
        self.retrasos()
        print("--------------------------------------------")
        print(f"Alumno que prestó el libro: {self.alumno}")
        print(f"Código del alumno: {self.codigo}")
        print(f"Nombre del libro: {self.libro}")
        print(f"Fecha de préstamo: {self.fecha}")
        print(f"Fecha de entrega o habrá sanción: {self.fechaentrega}")

# Ejemplo de uso
orden = Biblioteca()
orden.registro()  # Asegúrate de registrar primero para proporcionar los datos necesarios
orden.mostrardato()
