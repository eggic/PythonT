# Ejercicio 1 - Situación Problema:
# Este ejercicio está basado en una situación donde una veterinaria necesita un sistema para registrar la información de los perros que atienden,
# incluyendo detalles del perro y si ya ha sido atendido previamente. Esto permite llevar un control adecuado de la salud de los perros y mejorar el servicio.

class Perro:
    def __init__(self, nombre, raza, edad, peso, color, dueño, contacto, atendido):
        # Inicializa los atributos del perro con los valores proporcionados
        self.nombre = nombre  # Nombre del perro
        self.raza = raza  # Raza del perro
        self.edad = edad  # Edad del perro en años
        self.peso = peso  # Peso del perro en kg
        self.color = color  # Color del perro
        self.dueño = dueño  # Nombre del dueño del perro
        self.contacto = contacto  # Contacto del dueño
        # Determina si el perro ya ha sido atendido antes
        self.estado = "ATENDIDO" if atendido else "NO ATENDIDO"
        # Clasifica el tamaño del perro según su peso
        self.tamaño = "Perro grande" if peso >= 10 else "Perro pequeño"

    def registrar(self):
        # Llama a la función para mostrar la información registrada del perro
        self.mostrar_informacion()

    def mostrar_informacion(self):
        # Imprime en pantalla los datos registrados del perro
        print("-----------------------------------------")
        print("DATOS DEL CAHORRO:")
        print("-----------------------------------------")
        print(f"Nombre: {self.nombre}")  # Muestra el nombre del perro
        print(f"Raza: {self.raza}")  # Muestra la raza del perro
        print(f"Edad: {self.edad} años")  # Muestra la edad del perro
        print(f"Peso: {self.peso} kg ({self.tamaño})")  # Muestra el peso y tamaño del perro
        print(f"Color: {self.color}")  # Muestra el color del perro
        print(f"Dueño: {self.dueño}")  # Muestra el nombre del dueño
        print(f"Contacto del dueño: {self.contacto}")  # Muestra el contacto del dueño
        print(f"Estado: {self.estado}")  # Muestra si el perro ha sido atendido antes o no

# Solicita al usuario que ingrese los datos del perro
print("Bienvenido a la veterinaria para perros, ingrese los datos a continuación:")
atendido = input("¿El perro ha sido atendido antes en esta veterinaria? (si/no): ").strip().lower() == "si"
# Verifica si el perro ya ha sido atendido antes

# Recolecta la información básica del perro y del dueño
nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro: "))
peso = float(input("Ingrese el peso del perro: "))
color = input("Ingrese el color del perro: ")
dueño = input("Ingrese el nombre del dueño: ")
contacto = input("Ingrese el contacto del dueño: ")

# Crea un objeto de la clase Perro con los datos proporcionados
perro = Perro(nombre, raza, edad, peso, color, dueño, contacto, atendido)

# Registra y muestra la información del perro
perro.registrar()
