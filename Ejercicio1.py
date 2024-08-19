#Ejercicio 1
class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño, contacto, atendido):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.dueño = dueño
        self.contacto = contacto
        self.estado = "ATENDIDO" if atendido else "NO ATENDIDO"
        self.tamaño = "Perro grande" if peso >= 10 else "Perro pequeño"

    def registrar(self):
        self.mostrar_informacion()

    def mostrar_informacion(self):
        print("-----------------------------------------")
        print("Aqui estan los datos:")
        print("-----------------------------------------")
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg ({self.tamaño})")
        print(f"Color: {self.color}")
        print(f"Dueño: {self.dueño}")
        print(f"Contacto del dueño: {self.contacto}")
        print(f"Estado: {self.estado}")


print("Bienvenido a la veterinaria para perros, ingrese los datos a continuación:")
atendido = input("¿El perro ha sido atendido antes en esta veterinaria? (si/no): ").strip().lower() == "si"


nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro: "))
peso = float(input("Ingrese el peso del perro: "))
color = input("Ingrese el color del perro: ")
dueño = input("Ingrese el nombre del dueño: ")
contacto = input("Ingrese el contacto del dueño: ")

perro = Perro(nombre, raza, edad, peso, color, dueño, contacto, atendido)

perro.registrar()