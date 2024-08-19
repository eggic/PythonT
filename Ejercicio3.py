"""
#Situación Problemática:
Una concesionaria de autos vende vehículos de diferentes marcas, modelos y características.
El sistema necesita registrar las características principales de cada auto, calcular su precio 
de venta basado en un margen de ganancia del 40%, y generar un ticket que muestre un resumen de
la venta.

#Explicación del Código:
Este código permite registrar la información de un auto que se va a vender en una concesionaria.
Se le pide al usuario que ingrese los datos del auto, como marca, modelo, año, color, tipo, precio
de compra, número de puertas, tipo de motor, tipo de transmisión, y tipo de combustible. Luego, el
sistema calcula el precio de venta aplicando un margen de ganancia del 40% y genera un ticket con 
todos los detalles del auto, incluyendo el precio de venta.

"""
class Auto:
    def __init__(self, marca, modelo, año, color, tipo, precio_compra, numero_puertas, tipo_motor, tipo_transmision, tipo_combustible):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo  # Nacional o Importado
        self.precio_compra = precio_compra
        self.numero_puertas = numero_puertas
        self.tipo_motor = tipo_motor
        self.tipo_transmision = tipo_transmision
        self.tipo_combustible = tipo_combustible
        
        # Atributos fijos
        self.ruedas = 4
        self.capacidad_pasajeros = 5

    def calcular_precio_venta(self):
        return round(self.precio_compra * 1.4, 2)

    def generar_ticket(self):
        ticket = (
            f"--- TICKET DE VENTA ---\n"
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Año: {self.año}\n"
            f"Color: {self.color}\n"
            f"Tipo: {self.tipo}\n"
            f"Precio de Compra: ${self.precio_compra}\n"
            f"Número de Puertas: {self.numero_puertas}\n"
            f"Tipo de Motor: {self.tipo_motor}\n"
            f"Tipo de Transmisión: {self.tipo_transmision}\n"
            f"Tipo de Combustible: {self.tipo_combustible}\n"
            f"Ruedas: {self.ruedas}\n"
            f"Capacidad para Pasajeros: {self.capacidad_pasajeros}\n"
            f"Precio de Venta: ${self.calcular_precio_venta()}\n"
            f"------------------------"
        )
        return ticket

def registrar_auto():
    print("- TICKET DE COMPRA -")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    color = input("Color: ")
    tipo = input("Tipo (Nacional/Importado): ").capitalize()
    precio_compra = float(input("Precio de Compra: "))
    numero_puertas = int(input("Número de Puertas: "))
    tipo_motor = input("Tipo de Motor: ")
    tipo_transmision = input("Tipo de Transmisión: ")
    tipo_combustible = input("Tipo de Combustible: ")

    auto = Auto(marca, modelo, año, color, tipo, precio_compra, numero_puertas, tipo_motor, tipo_transmision, tipo_combustible)
    return auto

auto = registrar_auto()

ticket = auto.generar_ticket()
print("\n" + ticket)