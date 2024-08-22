class pasteria():
    cliente=""
    tipo_pastel=""
    tamano=0
    precio=0
    precioVenta=0
    factura=0
    fecha=""
    sabor=""

    def __init__(self):
        self.cliente=""
        self.tamano=0
        self.precio=10
        self.precioVenta=0
        self.factura=0
        self.fecha=""
        
        self.sabor=""

    def precioportamano(self):
        if (self.tamano==12):
            self.precioVenta=self.precio*1.2
            print(f"El precio del pastel mas chiquito es de ${self.precioVenta} dolares")
        elif(self.tamano==14):
            self.precioVenta=self.precio*1.4
            print(f"El precio del pastel mediano es de ${self.precioVenta} dolares")
        elif(self.tamano==20):
            self.precioVenta=self.precio*2.0
            print(f"El precio del pastel mas grande es de ${self.precioVenta} dolares")
        else:
            print("Ingresa un dato valido")

    def insertDatos(self):
        self.cliente = input("Ingrese el nombre del cliente > ")
        print("Los tamanos son: PEQUEÑO: 12, MEDIANO:14, GRANDE:20")
        self.tamano = int(input("Ingrese el número del pastel > "))
        self.fecha = input("Ingrese la fecha de entrega > ")
        self.sabor=input("Ingrese el sabor que desee > ") 

    def mostrarDatos(self):
        print("RECIBO")
        print(f"El nombre del cliente es {self.cliente}")
        print(f"El tamaño del pastel es {self.tamano}")
        print(f"El sabor del pastel es {self.sabor}")
        self.precioportamano()

Compra1 = pasteria()
print("PASTELERIA VALERIA")
Compra1.insertDatos()
print("--------------------------------------------------")
Compra1.mostrarDatos()
print("--------------------------------------------------")
print("GRACIAS POR SU COMPRA")
print("--------------------------------------------------")