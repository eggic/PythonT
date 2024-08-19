class Papeleria:
    def __init__(self):
        self.Cuaderno = ""
        self.Lapices = ""
        self.CantidadCuadernos = 0
        self.CantidadLapices = 0
        self.PrecioVenta = 0
        self.PrecioLapices = 0
        self.LlevasCuadernos = ""
        self.LlevasLapices = ""

    def TipoCuaderno(self):
        if self.Cuaderno == "grande":
            self.PrecioVenta = round((self.CantidadCuadernos * 3.50) * 1.30, 2)
            print(f"Llevas {self.CantidadCuadernos} cuaderno(s) grande(s) : ${self.PrecioVenta}.")
            print("Marca: Conquistador")
        elif self.Cuaderno == "pequeño":
            self.PrecioVenta = round((self.CantidadCuadernos * 1.75) * 1.30, 2)
            print(f"Llevas {self.CantidadCuadernos} cuaderno(s) pequeño(s) : ${self.PrecioVenta}.")
            print("Marca: Escribo")
        else:
            print("No reconozco esa respuesta")

    def TipoLapices(self):
        if self.Lapices == "grafito":
            self.PrecioLapices = round((self.CantidadLapices * 0.25) * 1.30, 2)
            print(f"Llevas {self.CantidadLapices} lápices de grafito y su precio es ${self.PrecioLapices}.")
            print("Marca: Facela")
        elif self.Lapices == "color":
            self.PrecioLapices = round((self.CantidadLapices * 0.50) * 1.30, 2)
            print(f"Llevas {self.CantidadLapices} lápices de color y su precio es ${self.PrecioLapices}.")
            print("Marca: FaberCatle")
        else:
            print("No reconozco esa respuesta")

    def DatosCompra(self):
        self.TipoCuaderno()
        self.TipoLapices()

    def RegistrarCompra(self):
        print("- Preparándote para la mejor experiencia de compra -")
        self.LlevasCuadernos = input("¿Llevarás cuadernos? (S/N): ").lower()
        if self.LlevasCuadernos == "s":
            self.Cuaderno = input("Tipo de cuaderno (grande/pequeño): ").lower()
            try:
                self.CantidadCuadernos = int(input("¿Cuántos cuadernos llevas?: "))
            except ValueError:
                print("Cantidad de cuadernos inválida. Se asignará 0.")
                self.CantidadCuadernos = 0
        else:
            print("Recuerda, tenemos cuadernos exclusivos marca Hojitas.")
        
        self.LlevasLapices = input("¿Llevarás lápices? (S/N): ").lower()
        if self.LlevasLapices == "s":
            self.Lapices = input("Tipo de lápiz (grafito/color): ").lower()
            try:
                self.CantidadLapices = int(input("¿Cuántos lápices llevas?: "))
            except ValueError:
                print("Cantidad de lápices inválida. Se asignará 0.")
                self.CantidadLapices = 0
        else:
            print("Recuerda, tenemos lápices exclusivos marca Rayitas.")
        

    def MostrarDatosCompras(self):
        print(" Resumen de tu compra ")
        print("Estado Cuadernos: ", self.LlevasCuadernos)
        if self.LlevasCuadernos == "s":
            self.TipoCuaderno()
        else:
            print("No llevas cuadernos.")

        print("Estado Lápices: ", self.LlevasLapices)
        if self.LlevasLapices == "s":
            self.TipoLapices()
        else:
            print("No llevas lápices.")


Compra1 = Papeleria()
print("- Bienvenido al sistema de compras -")
Compra1.RegistrarCompra()
print("-----------------------------------------")
Compra1.MostrarDatosCompras()
print("-----------------------------------------")
print("- Gracias por venir a la Papelería -")
print("-----------------------------------------")
