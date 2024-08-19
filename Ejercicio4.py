class DispositivoElectronico:
    def __init__(self, tipo, modelo, tamaño_pantalla, capacidad_almacenamiento, ram, precio_compra):
        self.tipo = tipo  
        self.modelo = modelo
        self.tamaño_pantalla = tamaño_pantalla
        self.capacidad_almacenamiento = capacidad_almacenamiento
        self.ram = ram
        self.precio_compra = precio_compra

    def calcular_precio_venta(self):
        return round(self.precio_compra * 1.7, 2)

    def generar_ticket(self):
        ticket = (
            f"--- TICKET DE VENTA ---\n"
            f"Tipo: {self.tipo}\n"
            f"Modelo: {self.modelo}\n"
            f"Tamaño de Pantalla: {self.tamaño_pantalla}\"\n"
            f"Capacidad de Almacenamiento: {self.capacidad_almacenamiento} GB\n"
            f"RAM: {self.ram} GB\n"
            f"Precio de Compra: ${self.precio_compra}\n"
            f"Precio de Venta: ${self.calcular_precio_venta()}\n"
            f"------------------------"
        )
        return ticket

def registrar_dispositivo():
    print("- Registro de Dispositivo Electrónico -")
    tipo = input("Marca (Celular/Tablet/Portátil): ").capitalize()
    modelo = input("Modelo: ")
    tamaño_pantalla = float(input("Tamaño de Pantalla (en pulgadas): "))
    capacidad_almacenamiento = int(input("Capacidad de Almacenamiento (en GB): "))
    ram = int(input("RAM (en GB): "))
    precio_compra = float(input("Precio de Compra: "))

    dispositivo = DispositivoElectronico(tipo, modelo, tamaño_pantalla, capacidad_almacenamiento, ram, precio_compra)
    return dispositivo

dispositivo = registrar_dispositivo()

ticket = dispositivo.generar_ticket()
print("\n" + ticket)