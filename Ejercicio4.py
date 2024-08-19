"""
Un almacén que vende dispositivos electrónicos de la nueva marca "PHR" necesita un sistema para 
registrar las características de los productos que venden (celulares, tablets y portátiles). Dado
que todos los productos son importados, el precio de venta se calcula multiplicando el precio de 
compra por 1.7. Además, el sistema creado permite registrar múltiples productos en una sola sesión,
generar un ticket de venta, y preguntar al comprador si desea registrar otro producto, esto en
el dado caso que se quiera utilizar el sistema para ejecutar un recibo
"""

class DispositivoElectronico:
    def __init__(self, tipo, modelo, tamaño_pantalla, capacidad_almacenamiento, ram, precio_compra):
        self.marca = "PHR"  # Todos los dispositivos son de la marca PHR
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
            f"Marca: {self.marca}\n"
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
    tipo = input("Tipo (Celular/Tablet/Portátil): ").capitalize()
    modelo = input("Modelo: ")
    tamaño_pantalla = float(input("Tamaño de Pantalla (en pulgadas): "))
    capacidad_almacenamiento = int(input("Capacidad de Almacenamiento (en GB): "))
    ram = int(input("RAM (en GB): "))
    precio_compra = float(input("Precio de Compra: "))

    dispositivo = DispositivoElectronico(tipo, modelo, tamaño_pantalla, capacidad_almacenamiento, ram, precio_compra)
    return dispositivo

def main():
    while True:
        dispositivo = registrar_dispositivo()
        ticket = dispositivo.generar_ticket()
        print("\n" + ticket)
        
        # Preguntar si el comprador desea registrar otro producto
        otra_compra = input("¿Deseas registrar otro producto? (S/N): ").lower()
        if otra_compra != 's':
            break

    print("Gracias por tu compra.")

# Ejecutar el programa
main()
